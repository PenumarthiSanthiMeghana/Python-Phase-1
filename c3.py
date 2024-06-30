def bfs(graph,start):
    que=[start]
    vis=[start]
    ele=0
    while(len(que)!=0):
       ele= que.pop(0)
       print(graph[ele])
       for node in graph[ele]:
           if node not in vis:
               que.append(node)
               vis.append(node)
    return vis
       
        
   
graph = {
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","E"],
    "D":["B","F"],
    "E":["C","F"],
    "F":["D","E"]  
}   
out=bfs(graph,"B")
print(out)
    