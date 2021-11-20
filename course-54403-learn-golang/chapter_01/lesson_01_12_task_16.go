package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n, count int
    fmt.Scan(&n)
    a := make([]int, n)
    for i:=0;i<n;i++{
        fmt.Scan(&a[i])
        if a[i]>0{count++}
    }
    fmt.Println(count)
}