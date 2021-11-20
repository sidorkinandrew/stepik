package main
import (
    "fmt"
    "strconv"
    "strings"
    "bufio"
    "os"
)

func main() {
    // здесь должен быть ваш код
    reader := bufio.NewReader(os.Stdin)
    s, _ := reader.ReadString('\n')
    s = strings.Trim(s, " ")
    s = strings.ReplaceAll(s, " ", "")
    s = strings.ReplaceAll(s, ",", ".")
    stringSlice := strings.Split(s, ";")
    res1, _ := strconv.ParseFloat(string(stringSlice[0]), 64)
    res2, _ := strconv.ParseFloat(string(stringSlice[1]), 64)
    fmt.Println(strconv.FormatFloat(res1/res2, 'f', 4, 64)) // 1.01
}