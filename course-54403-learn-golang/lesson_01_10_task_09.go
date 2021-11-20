package main

import "fmt"

func main() {
    var x,p,y,sum int
    fmt.Scan(&x, &p, &y)
    sum = x
    for i:=1; sum<y; i++ {
        sum += sum*p/100
        if (sum > y) {
            fmt.Println(i)
            break
        }
    }
}