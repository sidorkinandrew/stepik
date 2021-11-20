package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n int
    fmt.Scan(&n)
    for i:=1;i<=n;i*=2{
        fmt.Print(i, " ");
    }
}