
package main
import (
    . "fmt"
    "os"
    "bufio"
    "strings"
    "unicode"
    "unicode/utf8"
)

func main() {
    text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
    //fmt.Println(unicode.IsUpper(text[0])) // true
    //text = strings.Replace(text, "\n","", -1)
    text = strings.Trim(text, "\n\r")
    textRunes := []rune(text)
    if unicode.IsUpper(textRunes[0]) && textRunes[utf8.RuneCountInString(text)-1] == []rune(".")[0] {
        Println("Right")
    } else {
        Println("Wrong")
    }
}