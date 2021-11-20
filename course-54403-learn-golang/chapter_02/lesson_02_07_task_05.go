package main
import (
    "fmt"
//    "strings"
)

func main() {
    // здесь должен быть ваш код
    var s string
    fmt.Scan(&s)
    for _, sym := range s { //strings.Split(s, ""){
        a := sym-'0'
        fmt.Print(a*a)
    }
}