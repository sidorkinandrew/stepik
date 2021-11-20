package main
import "fmt"

func fib(n int) int {
    prevFibs := []int{0, 1}
    for i := 3; i <= n; i++ {
        nextFib := prevFibs[0] + prevFibs[1]
        prevFibs = []int{prevFibs[1], nextFib}
    }
    if n > 1 {
        return prevFibs[1]
    }
    return prevFibs[0]
}


func main() {
    // здесь должен быть ваш код
    var n int
    fmt.Scan(&n)
    for i:=0;fib(i)<=n;i++{
        if fib(i) == n {
            fmt.Println(i-1)
            return
        }
    }
     fmt.Println(-1)   
}