class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = []
    
    # 간선을 가중치 순으로 정렬
    edges.sort(key=lambda edge: edge[2])
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += weight
            mst_edges.append((u, v, weight))
    
    return mst_weight, mst_edges

# 주어진 그래프의 정점과 간선
# 정점: A=0, B=1, C=2, D=3, E=4로 매핑
edges = [
    (0, 2, 4),  # A - C: 4
    (0, 4, 2),  # A - E: 2
    (0, 1, 7),  # A - B: 7
    (1, 4, 4),  # B - E: 4
    (1, 3, 3),  # B - D: 3
    (2, 4, 3),  # C - E: 3
    (2, 3, 5),  # C - D: 5
    (4, 3, 6)   # E - D: 6
]

# 정점의 수는 5 (A, B, C, D, E)
n = 5
mst_weight, mst_edges = kruskal(n, edges)

print(f"MST의 가중치 합: {mst_weight}")
print("MST의 간선들:", mst_edges)
