import argparse
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Point
from itertools import cycle
import numpy as np


# Function to read the shapefile
def load_shapefile(path):
    gdf = gpd.read_file(path)
    return gdf


def calculate_angle(segment1, segment2):
    """Calculates the angle between two line segments."""

    def line_to_vector(segment):
        x, y = segment.xy
        return np.array([x[1] - x[0], y[1] - y[0]])

    vector1 = line_to_vector(segment1)
    vector2 = line_to_vector(segment2)

    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)

    dot_product = np.dot(unit_vector1, unit_vector2)
    angle = np.arccos(dot_product)

    return np.degrees(angle)


def find_touch_point(line1, line2):
    """Finds the touch point between two LineStrings if they touch."""
    if line1.touches(line2):
        for point in line1.coords:
            if Point(point).touches(line2):
                return Point(point)
    return None


def get_sub_segments_by_point(line, point):
    """Finds the segment in a LineString that contains a specific point."""
    for i in range(len(line.coords) - 1):
        segment = LineString([line.coords[i], line.coords[i + 1]])
        if segment.touches(point):
            return segment
    return None


def angle_at_touch_point(line1, line2):
    """Finds the angle between two LineStrings at their touch point."""
    touch_point = find_touch_point(line1, line2)
    if touch_point is not None:
        segment1 = get_sub_segments_by_point(line1, touch_point)
        segment2 = get_sub_segments_by_point(line2, touch_point)
        if segment1 and segment2:
            return calculate_angle(segment1, segment2)
    return None


# # Function to calculate the angle between two segments
# def calculate_angle(line1, line2):
#     def line_to_vector(line):
#         x, y = line.xy
#         return np.array([x[1] - x[0], y[1] - y[0]])
#
#     vector1 = line_to_vector(line1)
#     # print(vector1)
#
#     vector2 = line_to_vector(line2)
#     # print(vector2)
#
#     unit_vector1 = vector1 / np.linalg.norm(vector1)
#     unit_vector2 = vector2 / np.linalg.norm(vector2)
#
#     dot_product = np.dot(unit_vector1, unit_vector2)
#     angle = np.arccos(dot_product)
#     # print(np.degrees(angle))
#     return np.degrees(angle)


def line_to_segments(line):
    """Converts a LineString into individual segments."""
    segments = []
    for i in range(len(line.coords) - 1):
        segment = LineString([line.coords[i], line.coords[i + 1]])
        segments.append(segment)
    return segments


# def find_best_angle(line1, line2):
#     """Finds the best (smallest) angle between two LineStrings."""
#     segments1 = line_to_segments(line1)
#     segments2 = line_to_segments(line2)
#     best_angle = float('inf')
#     for segment1 in segments1:
#         for segment2 in segments2:
#             angle = angle_at_touch_point(segment1, segment2)
#             if angle < best_angle:
#                 best_angle = angle
#     return best_angle


# Function to check if two segments can be part of the same street
def can_be_same_street(line1, line2, angle_threshold=60):
    if line1.touches(line2):
        # return True
        angle = angle_at_touch_point(line1, line2)
        return angle < angle_threshold
    return False


# Function to group segments into streets based on continuity and angles
def group_segments(segments, angle_threshold=60):
    streets = []
    visited = set()

    def dfs(segment, street):
        visited.add(segment)
        street.append(segment)
        for neighbor in segments:
            if neighbor not in visited and can_be_same_street(segment, neighbor, angle_threshold):
                print('neighbor: ', neighbor)
                dfs(neighbor, street)

    for segment in segments:
        if segment not in visited:
            street = []
            print('head: ', segment)
            dfs(segment, street)
            streets.append(street)
            print('-----------------------------------')

    return streets


# Assign colors to each street
def assign_colors(streets, is_solid=False):
    colors = cycle(plt.cm.tab20.colors)
    line_styles = cycle(['solid'] if is_solid else ['solid', 'dashed', 'dashdot', 'dotted'])
    street_colors = []
    for street in streets:
        color = next(colors)
        line_style = next(line_styles)
        for segment in street:
            street_colors.append([segment, color, line_style])
    return street_colors


# Plot the streets with colors
def plot_streets(street_colors, output_path):
    plt.figure(figsize=(30, 30))

    for i, (segment, color, line_styles) in enumerate(street_colors):
        x, y = segment.xy
        plt.plot(x, y, color=color, linewidth=3, linestyle=line_styles)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add major and minor grid lines
    plt.minorticks_on()
    # plt.xlabel("Longitude", fontsize=28)  # Add x-axis label
    # plt.ylabel("Latitude", fontsize=28)  # Add y-axis label
    plt.xticks(fontsize=22)  # Set font size for x-axis ticks
    plt.yticks(fontsize=22)  # Set font size for y-axis ticks
    plt.axis('on')
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


# Main function
def main():
    parser = argparse.ArgumentParser(description="Street coloring script")
    parser.add_argument("--input", required=True, help="Path to the directory containing the shapefile")
    parser.add_argument("--output", required=True, help="Path for the output image")
    parser.add_argument("--solid", required=False, help="Is the output lines are solid (default True)")
    parser.add_argument("--angle_threshold", required=False,
                        help="Angle threshold for grouping segments to one street (default 60)")
    args = parser.parse_args()

    shapefile_path = args.input
    output_path = args.output
    angle_threshold = 60 if args.angle_threshold is None else int(args.angle_threshold)
    is_solid = str2bool(args.solid) if args.solid is not None else True
    gdf = load_shapefile(shapefile_path)
    segments = [geom for geom in gdf.geometry if isinstance(geom, LineString)]
    streets = group_segments(segments, angle_threshold=angle_threshold)
    street_colors = assign_colors(streets, is_solid=is_solid)
    plot_streets(street_colors, output_path)
    print(f"Street coloring completed. Check {output_path} for the result.")


if __name__ == "__main__":
    main()
