// Пакет и функция main уже объявлены.
// Выводить или вводить ничего не нужно!

func removeDuplicates(inputStream chan string, outputStream chan string) {
	var previous string
	previous = "starting"
	for value := range inputStream {
		if previous == "starting" {
			outputStream <- value
			previous = value
			continue
		}
		if value != previous {
			previous = value
			outputStream <- value
		}

	}
	close(outputStream)
}


