func fibonacci(n int) int {
    prevFibs := []int{1, 1}
    for i := 3; i <= n; i++ {
        nextFib := prevFibs[0] + prevFibs[1]
        prevFibs = []int{prevFibs[1], nextFib}
    }
    if n > 1 {
        return prevFibs[1]
    }
    return prevFibs[0]
}




