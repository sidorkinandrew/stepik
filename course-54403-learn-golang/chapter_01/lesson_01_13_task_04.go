package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n int
    fmt.Scan(&n)
    fmt.Println("It is",n/3600,"hours",n%3600/60,"minutes.")
}