package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var a, b int
    fmt.Scan(&a, &b)
    for ;b>=a;b--{
        if b % 7 == 0{
            fmt.Println(b)
            return
        }
    }
    fmt.Print("NO")
}