package main
import "fmt"

func main(){
  names := []byte{'g', 'o', 'l', 'a', 'n', 'g'}

  for _, v := range(names) {
      fmt.Println(v)
  }

  fmt.Println(len(names), cap(names))
}
