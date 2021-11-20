// Пакет и функция main уже объявлены, выводить и считывать ничего не нужно!

func task2(c chan string, s string) {
    c <- s + " "
    c <- s+ " "
    c <- s+ " "
    c <- s+ " "
    c <- s+ " "
}


