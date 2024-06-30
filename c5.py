def bfs(graph,start):
     que=[start]
     vis=[start]
     arr=[]
     while(len(arr)!=0):
         ele=que.pop(0)
         print(graph[ele])
         for node in graph(ele):
             if node not in que:
                 que=ele.append()
                 vis=ele.append()
                 print(vis)


graph={
    "A":["B","C"],
    "B":["A","D"],
    "C":["A","E"],
    "D":["B","F"],
    "E":["C","F"],
    "F":["D","E"]  
    
}
res=bfs(graph,"C")
print(res)
             
     