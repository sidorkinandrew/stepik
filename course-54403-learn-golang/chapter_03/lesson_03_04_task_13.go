package main

import (
    "fmt"
) // пакет используется для проверки ответа, не удаляйте его


type Battery struct {  // [      XXXX]: где пробелы - "опустошенная" емкость батареи, а X - "заряженная".
    Empty string
    Full string
    Data string
}

func (a Battery) String() string {
    for i:= range a.Data{
        if string(a.Data[i]) == "0"{
            a.Empty += " "
        }
        if string(a.Data[i]) == "1"{
            a.Full += "X"
        }
    }
	return fmt.Sprintf("[%s%s]", a.Empty, a.Full)
}

func main() {
    var s string
    fmt.Scan(&s)
    // batteryForTest - не забывайте об имени
    batteryForTest := Battery{
        Data: s,
    }
// } Скобка, закрывающая функцию main() вам не видна, но она есть