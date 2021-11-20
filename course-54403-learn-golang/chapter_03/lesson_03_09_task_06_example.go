package main

import (
	"fmt"
	"sync"
)

func main() {
	var x int
	wg := new(sync.WaitGroup)

	for i := 0; i < 1000; i++ {
		// Запускаем 1000 экземпляров горутины, увеличивающей счетчик на 1
		wg.Add(1)
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			x++
		}(wg)
	}

	wg.Wait()

	// По идее значение счетчика должно быть 1000, но крайне вероятно, что этого не произойдет
	fmt.Println(x)
}