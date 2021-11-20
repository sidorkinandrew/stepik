package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	tick := time.NewTicker(time.Second)
	defer tick.Stop()

	wg := new(sync.WaitGroup)

	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go worker(i, tick.C, wg)
	}

	wg.Wait()

	/*
	 * worker 1 выполнил работу
	 * worker 5 выполнил работу
	 * worker 3 выполнил работу
	 * worker 4 выполнил работу
	 * worker 2 выполнил работу
	 */
}

func worker(id int, limit <-chan time.Time, wg *sync.WaitGroup) {
	defer wg.Done()
	<-limit
	fmt.Printf("worker %d выполнил работу\n", id)
}