package main

import (
    "fmt"
    "strings"
    "bufio"
    "os"
    "time"
)

func main() {
    // put your code here
    buf, _ := bufio.NewReader(os.Stdin).ReadString('\n')
    buf = strings.TrimSpace(buf)
    firstTime, err := time.Parse(time.RFC3339, buf)
    if err != nil {
        panic(err)
    }
    fmt.Println(firstTime.Format(time.UnixDate))
}