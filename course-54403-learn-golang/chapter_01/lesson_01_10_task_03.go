package main

import "fmt"

func main() {
    var a,b int
    fmt.Scan(&a, &b)
    result := 0
    for i:=a; i<=b; i++ {
        result = result + i
        //fmt.Println(i)
    }
    fmt.Println(result)
}