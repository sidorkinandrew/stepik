type Bike struct{
  On bool
  Ammo int
  Power int
}
func (b *Bike) Shoot() bool {
      if !b.On || b.Ammo <=0 {return false}
      b.Ammo--
      return true
  }
func (b *Bike) RideBike() bool {
      if !b.On || b.Power <=0 {return false}
      b.Power--
      return true
  }

func main() {

  testStruct := new(Bike)
/*
 * Экземпляр созданной вами структуры необходимо передать в качестве
 * аргумента функции testStruct, которая выполнит проверку соблюдения
 * всех условий задания/
 */

// }