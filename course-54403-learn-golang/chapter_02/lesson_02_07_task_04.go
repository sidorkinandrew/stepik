package main
import (
    "fmt"
)

func main() {
    // здесь должен быть ваш код
    var s string
    var max rune
    fmt.Scan(&s)
    
    for i, sym := range s{
        if i == 0 || sym > max {
            max = sym
        }
    }
    fmt.Println(max-'0')
}