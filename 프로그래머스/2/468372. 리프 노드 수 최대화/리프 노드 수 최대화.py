def get_leaf_node_count(dist_limit: int, split_limit: int, child_counts: list[int], cur_depth_node_count: int):
    if dist_limit == 0:
        return cur_depth_node_count
    
    result = 0

    for child_count in child_counts:
        temp_result = 0

        if split_limit < child_count:
            temp_result = cur_depth_node_count
        else:
            choose_child_count = dist_limit if dist_limit <= cur_depth_node_count else cur_depth_node_count

            n_dist_limit = dist_limit - choose_child_count
            n_split_limit = split_limit // child_count

            n_depth_node_count = choose_child_count * child_count
            temp_result = get_leaf_node_count(n_dist_limit, n_split_limit, child_counts, n_depth_node_count) 
            temp_result += cur_depth_node_count - choose_child_count


        result = max(result, temp_result)

    return result

def solution(dist_limit, split_limit):
    child_counts = [2, 3]
    return get_leaf_node_count(dist_limit, split_limit, child_counts, 1)