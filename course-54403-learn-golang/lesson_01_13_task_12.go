package main
import "fmt"

func selo(n int) {
    switch {
        case n%10 == 0 || (n>10 && n<20):
            fmt.Println(n, "korov")
        case n%10 == 1:
            fmt.Println(n, "korova")
        case n%10 == 2 || n%10 == 3 || n%10 == 4:
            fmt.Println(n, "korovy")
    default:
            fmt.Println(n, "korov")
    }
}

func main() {
    // здесь должен быть ваш код
    var n int
    fmt.Scan(&n)
    selo(n)
}