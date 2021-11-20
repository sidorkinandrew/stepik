package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n, count, min int
    fmt.Scan(&n)
    a := make([]int, n)
    for i:=0;i<n;i++{
        fmt.Scan(&a[i]);
        if i == 0 || a[i] < min {
            min = a[i]; count = 1
        } else if min == a[i] {count++}
    }
    
    fmt.Println(count)
}