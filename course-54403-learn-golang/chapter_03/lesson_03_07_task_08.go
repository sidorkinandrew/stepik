package main



import (
    "fmt"
    "strings"
    "bufio"
    "os"
    "time"
)

func main() {
    // вам это понадобится
    const now = 1589570165
    
    // put your code here
    buf, _ := bufio.NewReader(os.Stdin).ReadString('\n')
    buf = strings.TrimSpace(buf)
    buf = strings.ReplaceAll(buf, " сек.","s")
    buf = strings.ReplaceAll(buf, " мин. ","m")
    
    dur, err := time.ParseDuration(buf)
    if err != nil {
        panic(err)
    }

    tm := time.Unix(now, 0)
    fmt.Println(tm.Add(dur).Format(time.UnixDate)) // 1
       
}