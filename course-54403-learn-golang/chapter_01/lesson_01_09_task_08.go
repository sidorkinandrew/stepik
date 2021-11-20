package main

import (
    "fmt"
)
func sum3(a int) int{
    return a/100 + a%100/10 + a%10
}
func main() {
    var n int
    fmt.Scan(&n)
    a := n/1000
    b := n%1000
    fmt.Println(func() string { if sum3(a) == sum3(b) { return "YES" } else { return "NO" } }())        
}