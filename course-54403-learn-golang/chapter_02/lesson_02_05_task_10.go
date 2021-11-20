package main

import (
    . "fmt"
    "strings"
)

func main() {
    var text string
    Scan(&text)
    text = strings.Trim(text, "\n\r")
    for i := range text{
        if i%2 == 1{
            Print(string(text[i]))
        }
    }
}