func test(x1 *int, x2 *int) {
  // здесь ваш код
   *x1, *x2 = *x2, *x1    
   fmt.Println(*x1, *x2)
}




