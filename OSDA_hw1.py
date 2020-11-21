#Question2
import itertools

def check_relation(relation_dict):
    for i in relation_dict:
        for j in relation_dict[i]:
            if i in relation_dict[j]:         # check asymmetric
                return False
            for k in relation_dict[j]:
                if k not in relation_dict[i]: # check transitive
                    return False
    return True
def count_relations(n):
    max_pairs_num = (n**2-n)//2
    pairs = [[i, j] for j in range(n) for i in range(n) if i != j]
    count = 0
    for pairs_num in range(max_pairs_num + 1):
        for relation_pairs in itertools.combinations(pairs, pairs_num):
            relation_dict = {i : [] for i in range(n)}
            for rp in relation_pairs:
                relation_dict[rp[0]].append(rp[1])
            if check_relation(relation_dict):
                count += 1
    print(count)
count_relations(5)


#Question3
def TopologicalSort(G):
    in_degrees = dict((u, 0) for u in G)    #1
    vertex_num = len(in_degrees)
    for u in G:                             #2
        for v in G[u]:
            in_degrees[v] += 1
    Q = [u for u in G if in_degrees[u] == 0]#3
    res = []
    while Q:
        u = Q.pop(0)                        #4
        res.append(u)
        for v in G[u]:
            in_degrees[v] -= 1              #5
            if in_degrees[v] == 0:          #6
                Q.append(v)
    if len(res) == vertex_num:
        return res
    else:
        print("there's a circle.")

graph = {
    "A": ["B","C"],
    "B": ["D","E"],
    "C": ["D","E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}
print(TopologicalSort(graph))

vertexes = ['A','B','C','D','E','F']
