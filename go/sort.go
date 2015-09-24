package main
import "fmt"

func insertionSort(values []int) []int{
  for i := 0; i < len(values); i++ {
    for j := i + 1; j < len(values); j++ {
      if values[j] < values[i] {
        values[i], values[j] = values[j], values[i]
      }
    }
  }
  return values
}

func 

func main(){
  values := []int{4, 6, 23, 67, 5, 3, 5, 7, 3, 5}

  fmt.Println("Insertion sort:", insertionSort(values))
}
