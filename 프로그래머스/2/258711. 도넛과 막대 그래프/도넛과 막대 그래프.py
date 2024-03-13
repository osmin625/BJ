def solution(edges):
    def make_graph():
        graph = {}
        node_cnt = 0
        for a, b in edges:
            if graph.get(a) is None:
                graph[a] = []
            graph[a].append(b)
            node_cnt = max(node_cnt, a, b)
        return graph, node_cnt


    def make_ind():
        ind = {}
        for a, b in edges:
            if ind.get(b) is None:
                ind[b] = 0
            ind[b] += 1
        return ind


    def find_gen_node():
        for n in range(1, node_cnt + 1):
            if graph.get(n) is not None and len(graph[n]) >= 2 and not ind.get(n):
                return n
        exit(1)
    
    def find_invalid_node():
        invalid = []
        for n in range(1, node_cnt + 1):
            if graph.get(n) is None and ind.get(n) is None:
                invalid.append(n)
        return invalid
    
    def remove_node():
        nonlocal graph, ind
        for n in graph.pop(gen_node):
            ind[n] -= 1
    
    def is_cycle(n):
        start = n
        while True:
            if ind[n] == 1 and graph.get(n,0) and len(graph.get(n)) == 1 and not visited[n]:
                visited[n] = 1
                n = graph.get(n)[0]
                if n == start:
                    return True
            else:
                return False
            
    def cal_cnt():
        nonlocal graph
        donut, stick, eight = 0, 0, 0
        for n in range(1, node_cnt + 1):
            if graph.get(n) is None:
                if n != gen_node and not ind.get(n, 0) and not n in invalid_node:
                    stick += 1
                continue
            if not ind.get(n, 0):
                stick += 1
            elif len(graph[n]) == ind.get(n) == 2:
                eight += 1
            elif is_cycle(n):
                donut += 1
        return donut, stick, eight
    
    graph, node_cnt = make_graph()
    visited = [0] * (node_cnt + 1)
    ind = make_ind()
    gen_node = find_gen_node()
    invalid_node = find_invalid_node()
    remove_node()
    donut, stick, eight = cal_cnt()
    answer = [gen_node, donut, stick, eight]
    return answer