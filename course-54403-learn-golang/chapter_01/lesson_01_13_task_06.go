package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var a, b, c int
    fmt.Scan(&a, &b, &c)
    check := a+b>c && b+c>a && a+c>b
    fmt.Println(func() string { if check { return "Существует" } else { return "Не существует" } }())
}