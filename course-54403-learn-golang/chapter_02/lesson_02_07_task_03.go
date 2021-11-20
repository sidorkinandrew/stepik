package main
import (
    "fmt"
    "strings"
)

func main() {
    // здесь должен быть ваш код
    var s string
    fmt.Scan(&s)
    fmt.Println(strings.Join(strings.Split(s, ""), "*"))
}