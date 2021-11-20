func calculator(firstChan <-chan int, secondChan <-chan int, stopChan <-chan struct{}) <-chan int {
    done := make(chan int)
    go func(firstChan <-chan int, secondChan <-chan int, stopChan <-chan struct{}, result chan<- int){
        defer close(result)
        select {
            case x := <-firstChan:
                result <- x*x
            case x:= <-secondChan:
                result <- x*3
            case <-stopChan:
                return
        }
    }(firstChan, secondChan, stopChan, done)
    return done
}