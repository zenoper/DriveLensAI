from typing import List, Tuple

def get_edges(polygon: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Returns a list of vectors representing the edges of the polygon."""
    edges = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        edges.append((p2[0] - p1[0], p2[1] - p1[1]))
    return edges

def get_perpendicular(vector: Tuple[float, float]) -> Tuple[float, float]:
    """Returns a vector perpendicular to the input vector."""
    return (-vector[1], vector[0])

def project_polygon(polygon: List[Tuple[float, float]], axis: Tuple[float, float]) -> Tuple[float, float]:
    """Projects a polygon onto an axis and returns the min/max values."""
    dots = []
    for vertex in polygon:
        dot_product = vertex[0] * axis[0] + vertex[1] * axis[1]
        dots.append(dot_product)
    return min(dots), max(dots)

def check_polygon_collision(polygon1: List[Tuple[float, float]], polygon2: List[Tuple[float, float]]) -> bool:
    """
    Check if two polygons are colliding using the Separating Axis Theorem.
    
    Args:
        polygon1: List of (x, y) tuples representing vertices of first polygon
        polygon2: List of (x, y) tuples representing vertices of second polygon
        
    Returns:
        bool: True if polygons are colliding, False otherwise
    """
    # Get all edges from both polygons
    edges1 = get_edges(polygon1)
    edges2 = get_edges(polygon2)
    edges = edges1 + edges2
    
    # Check each edge's perpendicular as a potential separating axis
    for edge in edges:
        # Get the perpendicular vector to use as projection axis
        axis = get_perpendicular(edge)
        
        # Project both polygons onto the axis
        proj1 = project_polygon(polygon1, axis)
        proj2 = project_polygon(polygon2, axis)
        
        # Check for separation
        if proj1[1] < proj2[0] or proj2[1] < proj1[0]:
            # Found a separating axis, polygons are not colliding
            return False
            
    # No separating axis found, polygons are colliding
    return True

# Example usage:
if __name__ == "__main__":
    # Test case 1: Overlapping polygons
    polygon1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    polygon2 = [(2, 2), (6, 2), (6, 6), (2, 6)]
    print(check_polygon_collision(polygon1, polygon2))  # Should print: True
    
    # Test case 2: Non-overlapping polygons
    polygon3 = [(5, 5), (7, 5), (7, 7), (5, 7)]
    print(check_polygon_collision(polygon1, polygon3))  # Should print: False
