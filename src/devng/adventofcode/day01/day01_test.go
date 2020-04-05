package main

import "testing"

func TestCountFloor(t *testing.T) {
	c1 := CountFloor("(())")
	if c1 != 0 {
		t.Error("Wrong c1 value.")
	}

	c2 := CountFloor("))(((((")
	if c2 != 3 {
		t.Error("Wrong c2 value.")
	}

	c3 := CountFloor(")())())")
	if c3 != -3 {
		t.Error("Wrong c3 value.")
	}
}

func TestFindBasement(t *testing.T) {
	b1 := FindBasement(")")
	if b1 != 1 {
		t.Error("Wrong b1 value.")
	}

	b2 := FindBasement("()())")
	if b2 != 5 {
		t.Error("Wrong b2 value.")
	}
}
