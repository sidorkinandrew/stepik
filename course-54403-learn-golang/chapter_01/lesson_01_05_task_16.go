package main
import "fmt"
func main(){

  var a int
  fmt.Scan(&a) // считаем переменную 'a' с консоли
  
  fmt.Println("It is",a/30,"hours",a%30*2,"minutes.")
}