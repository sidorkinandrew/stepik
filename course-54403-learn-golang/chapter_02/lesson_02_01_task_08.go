func vote(x int, y int, z int) int {
    test := (x + y + z) >= 2
    return func() int { if test { return 1 } else { return 0 } }()
}




