package main

import "fmt"

func main() {
    var a, _max, num int
    for fmt.Scan(&a); a != 0; fmt.Scan(&a){
        if a>_max {
            _max = a
            num = 1
        } else if a == _max {
            num += 1
        }
        
    }
    fmt.Println(num)
}