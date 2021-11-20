
package main
import (
    "fmt"
    "encoding/json"
    "io/ioutil"
    "os"
)

type (
    Student struct {
        LastName string
        FirstName string
        MiddleName string
        Birthday string
        Address string
        Phone string
        Rating []int
    }

    Group struct {
        ID int
        Number string
        Year string
	Students []Student
    }

    Rating struct {
	Average float32
    }
)

func main() {
    data, err := ioutil.ReadAll(os.Stdin)

    if err != nil {
        return
    }

    var group Group

    json.Unmarshal(data, &group)
    
    var marks, count float32

    for i := range group.Students {
        count++
        for range group.Students[i].Rating{
	    marks++}
    }
    var res Rating
    res.Average = marks / count

    result, _ := json.MarshalIndent(res, "", "    ")
    fmt.Printf("%s", result)
    
}