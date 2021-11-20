// вы уже внутри main()

done := make(chan struct{})

go func(d chan struct{}) {
    work()
    close(d)
}(done)

<-done

