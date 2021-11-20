package main

import (
    . "fmt"
    "strings"
    "unicode"
    "unicode/utf8"
)

func main() {
    var text string
    Scan(&text)
    text = strings.Trim(text, "\n\r")
    textRunes := []rune(text)
    if utf8.RuneCountInString(text) < 5{
        Print("Wrong password")
        return
    }
    for _, rune := range textRunes{
        if unicode.IsDigit(rune) || unicode.Is(unicode.Latin, rune){
            continue
        } else {
            Print("Wrong password")
            return
        }
    }
    Print("Ok")
}