func calculator(arguments <-chan int, done <-chan struct{}) <-chan int {
    result := make(chan int)
    var sum int
    go func(arguments <-chan int, done <-chan struct{}, result chan int, sum int) {
        defer close(result)
        for {
        select {
            case x := <-arguments:
                sum += x
            case <-done:
                result <- sum
                close(result)    
        }
        }
    }(arguments, done, result, sum)
    return result
}
