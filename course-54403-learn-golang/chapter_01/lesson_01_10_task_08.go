package main

import "fmt"

func main() {
    var n int
    for fmt.Scan(&n); n <= 100; fmt.Scan(&n){
        if n < 10{
            continue
        }
        fmt.Println(n)
    }
}