package main

import (
   "encoding/json"
   "fmt"
   "net/http"
)

type Data []struct {
   GlobalID       int    `json:"global_id"`
   SystemObjectID string `json:"system_object_id"`
   SignatureDate  string `json:"signature_date"`
   Razdel         string `json:"Razdel"`
   Kod            string `json:"Kod,omitempty"`
   Name           string `json:"Name"`
   Idx            string `json:"Idx"`
   Nomdescr       string `json:"Nomdescr,omitempty"`
}

func main(){
   var jsonData Data
   var url = "https://raw.githubusercontent.com/semyon-dev/stepik-go/master/work_with_json/data-20190514T0100.json"
   var result int

   resp, _ := http.Get(url)
   defer resp.Body.Close()

   r := json.NewDecoder(resp.Body)

   r.Decode(&jsonData)

   for _, val := range jsonData{
      result += val.GlobalID
   }

   fmt.Println(result)
}