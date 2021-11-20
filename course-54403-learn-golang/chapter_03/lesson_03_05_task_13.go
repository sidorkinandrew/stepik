package main

import (
   "archive/zip"
   "encoding/csv"
   "fmt"
)

func main() {
   r, _ := zip.OpenReader("task.zip")
   defer r.Close()

   for _, file := range r.File {
      if !file.FileInfo().IsDir() {
         fr, _ := file.Open()

         if data, _ := csv.NewReader(fr).ReadAll(); len(data) == 10 {
            fmt.Print(data[4][2])
         }

         fr.Close()
      }
   }
}