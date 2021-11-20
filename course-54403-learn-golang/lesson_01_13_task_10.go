package main
import "fmt"

func main() {
    // здесь должен быть ваш код
    var n, sum int
    fmt.Scan(&n)
    for ; n > 0; {
        for ;n>0;n=n/10{
            sum += n%10
        }
        if sum > 10 {
            n = sum
            sum = 0 
        }
    }
    fmt.Println(sum)
}