def is_color_safe(graph, current_node, colors_assignment, color_to_try):

    for connected_node in range(len(graph)):
        if graph[current_node][connected_node] == 1 and colors_assignment[connected_node] == color_to_try:
            return False

    return True

def try_color_graph(graph, max_colors, colors_assignment, current_node):

    if current_node == len(graph):
        return True

    for color in range(1, max_colors + 1):

        if is_color_safe(graph, current_node, colors_assignment, color):
            colors_assignment[current_node] = color

            if try_color_graph(graph, max_colors, colors_assignment, current_node + 1):
                return True

            colors_assignment[current_node] = 0

    return False


def find_min_colors_solution(graph):

    total_nodes = len(graph)
    colors_assignment = [0] * total_nodes

    for max_colors in range(1, total_nodes + 1):

        if try_color_graph(graph, max_colors, colors_assignment, 0):
            return max_colors, colors_assignment


graph_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

min_colors_count, final_colors = find_min_colors_solution(graph_matrix)

print(f"Минимальное количество цветов: {min_colors_count}")
print(f"Раскраска точек (номер точки : цвет):")
for node_index, color in enumerate(final_colors):
    print(f"Точка {node_index} -> Цвет {color}")