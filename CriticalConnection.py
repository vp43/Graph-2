"""1192. Critical Connections in a Network
TC:O(V+E)
SC:O(E)"""
# 2 Questions: what is the discovery order? what is earliest node that I can reach from a current node

class Solution:
    def __init__(self):
        self.graph=[]                                                
        self.result=[]                                                    
        self.time=0     
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
                                                         
        self.buildgraph(connections,n)                                          
        discovery=[-1]*n                                                        
        lowest=[0]*n                                                            
        self.dfs(0,0,discovery,lowest)                                          
        return self.result

    def buildgraph(self,connections,n):
        for i in range(n):                                                      
            self.graph.append([])
        for edge in connections:                                                
            self.graph[edge[0]].append(edge[1])                                       
            self.graph[edge[1]].append(edge[0])

    def dfs(self,v,u,discovery,lowest)->None:
        if discovery[v]!=-1:                                                    
            return
        discovery[v]=self.time                                                  
        lowest[v]=self.time                                                     
        self.time+=1                                                            
        neighbors=self.graph[v]                                                 
        for n in neighbors:                                                     
            if n==u:                                                            
                continue
            self.dfs(n,v,discovery,lowest)                                      
            if lowest[n]>discovery[v]:                                          
                self.result.append([v,n])                                       
            lowest[v]=min(lowest[v],lowest[n])                                  