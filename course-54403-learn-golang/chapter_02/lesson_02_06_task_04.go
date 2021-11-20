func main() {
    var a,b int
    fmt.Scan(&a, &b)
    d, err := divide(a, b)
    if err != nil {
	    fmt.Println("ошибка") // Функция вернула непустую ошибку
    } else {
	    fmt.Println(d) // Деление прошло без ошибок
    }

}


