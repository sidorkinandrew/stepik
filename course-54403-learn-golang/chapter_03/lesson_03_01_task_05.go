m := make(map[int]int)

var s string
var n int

for i:=0;i<10;i++{
    fmt.Scan(&s)
    if _, err := fmt.Sscan(string(s), &n); err == nil {
        if value, inMap := m[n]; inMap {
            fmt.Print(value, " ")
        } else {
            m[n] = work(n)
            fmt.Print(m[n], " ")
        }
    } else {
        fmt.Println(err)   
    }
}



