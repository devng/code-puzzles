package main

import "fmt"

// SumN returns the sum of the first n numbers.
func SumN(n int) int {
	return (n*n + n) / 2
}

// Sum35 finds the sum of all the multiples of 3 or 5 below the given limit.
func Sum35(limit int) int {
	limit = limit - 1
	sum3 := SumN(limit/3) * 3
	sum5 := SumN(limit/5) * 5
	sum15 := SumN(limit/15) * 15
	result := sum3 + sum5 - sum15
	return result
}

func main() {
	result := Sum35(1000)
	fmt.Println(result)
}
