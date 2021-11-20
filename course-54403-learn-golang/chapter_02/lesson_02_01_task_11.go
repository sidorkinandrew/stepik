/* ЗАДАНИЕ:
 * Напишите функцию sumInt, получающую переменное число аргументов типа int,
 * и возвращающую количество переданных аргументов и их сумму.
 */


 func sumInt(a ...int) (int, int) {
    sum := 0
    for _, elem := range a {
		sum += elem
	}
    return len(a), sum
}

