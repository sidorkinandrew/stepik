package main  
  
import (  
 "fmt"  
)

func isLeapYear(year int) bool {  
 leapFlag := false  
 if year%4 == 0 {  
  if year%100 == 0 {  
   if year%400 == 0 {  
    leapFlag = true  
   } else {  
    leapFlag = false  
   }  
  } else {  
   leapFlag = true  
  }  
 } else {  
  leapFlag = false  
 }  
 return leapFlag  
}  

func main() {  
    var n int
    fmt.Scan(&n)
    fmt.Println(func() string { if isLeapYear(n) { return "YES" } else { return "NO" } }()) 
}