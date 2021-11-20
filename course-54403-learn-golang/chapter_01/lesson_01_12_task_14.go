package main
import "fmt"

func main()  {
	array := [5]int{}
	var a int
	for i:=0; i < 5; i++{
		fmt.Scan(&a)
		array[i] = a
	}
    max := array[0]
    for _, m := range array{
         if max < m {
            max = m
        }
    }
    fmt.Println(max)
}