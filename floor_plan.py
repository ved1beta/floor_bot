import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

class SimpleFloorPlan:
    def __init__(self):
        self.points = None
        
    def create_simple_room(self, width=5, length=7, height=3):
        """Create a simple room with four walls"""
        # Create wall points
        walls = []
        
        # Floor points
        for x in np.linspace(0, width, 20):
            for z in np.linspace(0, length, 20):
                walls.append([x, 0, z])  # Floor
                walls.append([x, height, z])  # Ceiling
        
        # Wall points
        for y in np.linspace(0, height, 20):
            # Front and back walls
            for x in np.linspace(0, width, 20):
                walls.append([x, y, 0])  # Front wall
                walls.append([x, y, length])  # Back wall
            
            # Left and right walls
            for z in np.linspace(0, length, 20):
                walls.append([0, y, z])  # Left wall
                walls.append([width, y, z])  # Right wall
        
        self.points = np.array(walls)
        return self.points
    
    def visualize_3d(self):
        """Visualize the room in 3D"""
        if self.points is None:
            print("No points to visualize!")
            return
            
        # Create point cloud
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(self.points)
        
        # Visualize
        o3d.visualization.draw_geometries([pcd])
    
    def create_floor_slice(self, height=1.0, tolerance=0.1):
        """Extract points at a specific height (like taking a horizontal slice)"""
        if self.points is None:
            print("No points available!")
            return None
            
        # Find points near the specified height
        mask = np.abs(self.points[:, 1] - height) < tolerance
        slice_points = self.points[mask]
        
        return slice_points
    
    def visualize_2d_slice(self, slice_points):
        """Visualize the floor plan slice in 2D"""
        if slice_points is None or len(slice_points) == 0:
            print("No slice points to visualize!")
            return
            
        plt.figure(figsize=(10, 10))
        plt.scatter(slice_points[:, 0], slice_points[:, 2], c='blue', s=1)
        plt.title('Floor Plan Slice (Top View)')
        plt.xlabel('X axis')
        plt.ylabel('Z axis')
        plt.axis('equal')
        plt.grid(True)
        plt.show()

def main():
    # Create and visualize a simple room
    floor_plan = SimpleFloorPlan()
    
    # Create room points
    floor_plan.create_simple_room()
    
    # Visualize in 3D
    print("Showing 3D visualization...")
    floor_plan.visualize_3d()
    
    # Create and visualize a slice
    print("Creating floor plan slice...")
    slice_points = floor_plan.create_floor_slice(height=1.5)
    floor_plan.visualize_2d_slice(slice_points)

if __name__ == "__main__":
    main()
    