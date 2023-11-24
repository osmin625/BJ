import sys
sys.setrecursionlimit(10**6)


def find_root(nodes):
    return max(nodes,key=lambda x:x[2])

def divide_nodes(nodes,x):
    for idx in range(len(nodes)):
        if nodes[idx][1] == x:
            return nodes[:idx], nodes[idx+1:]

def solution(nodeinfo):
    nodes = [[i+1,x,y] for i,[x,y] in enumerate(nodeinfo)]
    nodes.sort(key=lambda x:x[1])
    pre_out, post_out = [], []
    def make_tree(nodes):
        if not nodes:return
        i, x, y = find_root(nodes)
        pre_out.append(i)
        left, right = divide_nodes(nodes,x)
        make_tree(left)
        make_tree(right)
        post_out.append(i)
    make_tree(nodes)
    
    return [pre_out, post_out]