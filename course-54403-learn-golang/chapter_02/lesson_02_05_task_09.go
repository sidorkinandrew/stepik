package main

import (
    . "fmt"
    "strings"
)

func main() {
    var text, part string
    Scan(&text)
    Scan(&part)
    text = strings.Trim(text, "\n\r")
    part = strings.Trim(part, "\n\r")
    Println(strings.Index(text, part))
}