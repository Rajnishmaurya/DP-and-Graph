class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list=defaultdict(list)

        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited=set()
        count=0

        def dfs(node,node_count):
            visited.add(node)
            node_data[0]+=1
            node_data[1]+=len(adj_list[node])

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour,node_data)
    
        for node in range(n):
            if node not in visited:
                node_data=[0,0] # node_count,degree_sum
                dfs(node,node_data)
                node_count,degree_sum=node_data

                if degree_sum==node_count*(node_count-1):
                    count+=1
        return count
        