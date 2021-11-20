package main

import(
    "fmt"
    "io"
    "bufio"
    "strings"
    "os"
    "time"
)


func main() {
    // put your code here
    inputTime, err := bufio.NewReader(os.Stdin).ReadString('\n')
    if err != nil && err != io.EOF { panic(err) }

    //Разделяем строку на подстроки по разделителю " , "
    inputTime = strings.TrimSpace(inputTime)
    inputs := strings.Split(inputTime, ",")

    s1, s2 := inputs[0], inputs[1]    
    secondTime, _ := time.Parse("02.01.2006 15:04:05", s1)
    firstTime, _ := time.Parse("02.01.2006 15:04:05", s2)
    
    if secondTime.After(firstTime){
        fmt.Println(secondTime.Sub(firstTime))
    } else {
        fmt.Println(firstTime.Sub(secondTime))
    }
    //fmt.Println(firstTime, s1, inputs[0])
    //fmt.Println(secondTime, s2, inputs[0])
    
}