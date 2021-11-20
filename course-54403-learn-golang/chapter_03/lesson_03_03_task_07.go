// fn

fn := func(num uint) uint { 
    s := fmt.Sprintf("%d", num)
    res := ""
    for i := range s{
        inum, _ := strconv.ParseUint(string(s[i]), 10, 8)
        if inum % 2 == 0 && inum>0{
            res += string(s[i])
        }
    }
    res1, _ := strconv.ParseUint(res, 10, 32)
    if res1 == 0{res1=100}
    return uint(res1)
}



