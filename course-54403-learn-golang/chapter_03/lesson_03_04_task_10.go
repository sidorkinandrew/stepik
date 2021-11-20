package main

import (
	"encoding/json" // пакет используется для проверки ответа, не удаляйте его
	"fmt"           // пакет используется для проверки ответа, не удаляйте его
	"os"            // пакет используется для проверки ответа, не удаляйте его
    "errors"
)

func check_float(i interface{}) (float64, error){
	switch v := i.(type) {
	case float64:
        return float64(v), nil
	default:
        return 0.0, fmt.Errorf("value=%v: %T", v, v)
	}
}

func check_operation(i interface{}) (string, error){
	switch v := i.(type) {
	case string:
        switch v{
            case "+","-","*","/":
                return string(v), nil
            default:
                return "", errors.New("неизвестная операция")
        }
	default:
        return "", fmt.Errorf("value=%v: %T", v, v)
	}
}


func main() {
	value1, value2, operation := readTask() // исходные данные получаются с помощью этой функции
                                            // все полученные значения имеют тип пустого интерфейса
    val1, err := check_float(value1)
    if err!=nil{
        fmt.Println(err)
        return
    }
    val2, err := check_float(value2)
    if err!=nil{
        fmt.Println(err)
        return
    }
    oper, err := check_operation(operation)
    if err!=nil{
        fmt.Println(err)
        return
    }
    switch oper{
    case "+":
        fmt.Printf("%.4f", val1 + val2)
    case "-":
        fmt.Printf("%.4f", val1 - val2)
    case "*":
        fmt.Printf("%.4f", val1 * val2)
    case "/":
        fmt.Printf("%.4f", val1 / val2)
    }
   
}