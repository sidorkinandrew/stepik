package main

import (
	"fmt"
	"time"
)

func main() {
	<-work()
	/*
	 * тик-так
	 * тик-так
	 * тик-так
	 * тик-так
	 */
}

func work() <-chan struct{} {
	done := make(chan struct{}) // канал для синхронизации горутин

	go func() {
		defer close(done) // синхронизирующий канал будет закрыт, когда функция завершит свою работу

		stop := time.NewTimer(time.Second)

		tick := time.NewTicker(time.Millisecond * 200)
		defer tick.Stop() // освободим ресурсы, при завершении работы функции

		for {
			select {
			case <-stop.C:
				// stop - Timer, который через 1 секунду даст сигнал завершить работу
				return
			case <-tick.C:
				// tick - Ticker, посылающий сигнал выполнить работу каждый 200 миллисекунд
				fmt.Println("тик-так")
			}
		}
	}()

	return done
}