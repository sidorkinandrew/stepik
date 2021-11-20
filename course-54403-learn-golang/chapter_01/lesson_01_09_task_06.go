package main

import "fmt"

func main() {
    var n int
    fmt.Scan(&n)
    n1:=n/100
    n2:=n%100/10
    n3:=n%10
    //fmt.Println(n1==n2, n2==n3, n1==n3)
    if n1==n2 || n2==n3 || n1==n3 {
      fmt.Println("NO")
    } else {
      fmt.Println("YES")        
    }
}