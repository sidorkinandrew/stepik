package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n int
    fmt.Scan(&n)
    var s string = fmt.Sprintf("%v",n)

    for i:=len(s)-1;i>=0;i--{
        fmt.Print(string(s[i]))
    }
    
}