package main

import "testing"

func TestSumN(t *testing.T) {
	sum10 := SumN(10)
	if sum10 != 55 {
		t.Error("The sum of the first 10 numbers must be 55.")
	}

	sum1000 := SumN(1000)
	if sum1000 != 500500 {
		t.Error("The sum of the first 10 numbers must be 500500.")
	}
}

func TestSum35(t *testing.T) {
	sum10 := Sum35(10)
	if sum10 != 23 {
		t.Error("The sum of multiples of 3 and 5 for the first 10 numbers must be 23.")
	}

	sum1000 := Sum35(1000)
	if sum1000 != 233168 {
		t.Error("The sum of multiples of 3 and 5 for the first 10 numbers must be 233168.")
	}
}
