package main

import "time"
import "fmt"

// CountSundays counts how many Sundays fell on the first of the month during a given period.
func CountSundays(fromYear int, toYear int) int {
  sundays := 0

  for year := fromYear; year < toYear; year++ {
    for month := 1; month < 13; month++ {
      t := time.Date(year, time.Month(month), 1, 0, 0, 0, 0, time.UTC)
      if t.Weekday() == time.Sunday {
        sundays++
      }
    }
  }
  return sundays
}

func main() {
  fmt.Println(CountSundays(1901, 2001))
}
