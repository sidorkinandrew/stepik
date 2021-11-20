package main

import "fmt"

func main() {
    var n, sum, _temp int
    fmt.Scan(&n)
    for i:=0; i<n; i++ {
        fmt.Scan(&_temp)      
        if (_temp % 8 == 0)&&(_temp > 9)&&(_temp < 100){
            sum += _temp
        }
    }
    fmt.Println(sum)
}