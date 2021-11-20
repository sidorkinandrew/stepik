package main
import (
   "bufio" //encoding/csv"
   "fmt"
   "net/http"
   "strings"
)

func main(){
   urlDownload := "https://raw.githubusercontent.com/semyon-dev/stepik-go/master/work_with_files/task_sep_1/task.data"
   resp, err := http.Get(urlDownload)
   if err != nil {
      return
   }
   defer resp.Body.Close()

   rdr, _ := bufio.NewReader(resp.Body).ReadString('\n')
   splitText := strings.Split(rdr, ";")

   for q, w := range splitText {
        if w == "0" {
            fmt.Println(q + 1)
        }
    }
}