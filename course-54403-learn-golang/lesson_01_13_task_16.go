package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n int
    var rem byte
    fmt.Scan(&n, &rem)
    var s string = fmt.Sprintf("%v",n)

    for i:=0;i<len(s);i++{
        //if string(s[i]) == string(rem){
        if s[i] != rem+'0'{
            fmt.Print(string(s[i]))
        }
    }
}