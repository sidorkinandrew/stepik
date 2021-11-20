// workArray := ...
workArray := [10]byte{}
    
for i,_:= range workArray{
    fmt.Scan(&workArray[i])
}
var a,b int
fmt.Scan(&a, &b)
workArray[a], workArray[b] = workArray[b], workArray[a]
fmt.Scan(&a, &b)
workArray[a], workArray[b] = workArray[b], workArray[a]
fmt.Scan(&a, &b)
workArray[a], workArray[b] = workArray[b], workArray[a]

for i,_:= range workArray{
    fmt.Print(workArray[i], " ")
}

