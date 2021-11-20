// Пакет и функция main уже объявлены!
// Импортировать ничего не нужно!
// Удачи!
func fetch_digits(a string) (string){
    var res string
    for i:=range a{
        switch a[i]{
            case '0','1','2','3','4','5','6','7','8','9':
            res += string(a[i])
        }
    }
    return res
}
func adding(a,b string) (int64){
    res1, _ := strconv.ParseInt(fetch_digits(a), 10, 64)
    res2, _:= strconv.ParseInt(fetch_digits(b), 10, 64)
    return res1 + res2
}


