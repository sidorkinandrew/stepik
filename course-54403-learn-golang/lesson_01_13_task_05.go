package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var a, b, c int
    fmt.Scan(&a, &b, &c)
    check := a*a+b*b==c*c || b*b+c*c==a*a || a*a+c*c==b*b
    fmt.Println(func() string { if check { return "Прямоугольный" } else { return "Непрямоугольный" } }())
}