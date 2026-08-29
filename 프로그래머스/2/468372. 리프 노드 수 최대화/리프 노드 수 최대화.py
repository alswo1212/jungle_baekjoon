def get_leaf_node_count(
    dist_limit: int, 
    split_limit: int, 
    cur_depth_node_count: int,
    used_3: bool
):
    if dist_limit == 0:
        return cur_depth_node_count
    
    answer = 0

    choose_node_count = dist_limit if cur_depth_node_count >= dist_limit else cur_depth_node_count
    n_dist_limit = dist_limit - choose_node_count
    remain_node_count = cur_depth_node_count - choose_node_count

    if not used_3 and split_limit >= 2:
        answer = max(
            get_leaf_node_count(n_dist_limit, split_limit // 2, choose_node_count * 2, False) + remain_node_count,
            answer
        )

    if split_limit >= 3:
        answer = max(
            get_leaf_node_count(n_dist_limit, split_limit // 3, choose_node_count * 3, True) + remain_node_count,
            answer
        )

    if split_limit < 2:
        answer += cur_depth_node_count

    return answer


def solution(dist_limit, split_limit):
    return get_leaf_node_count(dist_limit, split_limit, 1, False)