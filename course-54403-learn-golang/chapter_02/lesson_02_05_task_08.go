package main

import (
    . "fmt"
    "os"
    "bufio"
    "strings"
)

func main() {
    text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
    text = strings.Trim(text, "\n\r")
    //Println(strings.Split(text, ""))
    textRunes := []rune(text)
    _len := len(textRunes)
    r := make([]rune, _len)
    for _, rune := range textRunes {
        _len--
        r[_len] = rune
    }
    //Printf("%v, type: %T, len: %d\n",textRunes, textRunes, len(textRunes))
    //Printf("%v, type: %T, len: %d\n", r, r, len(r))
    if string(textRunes) == string(r) {
        Println("Палиндром")
    } else {
        Println("Нет")
    }
}