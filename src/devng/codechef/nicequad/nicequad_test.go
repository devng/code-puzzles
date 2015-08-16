package main

import "testing"

func TestPointQuadrant(t *testing.T) {
	p1 := Point{1, 1}
	q1 := p1.Quadrant()
	if q1 != 1 {
		t.Error("p1 is not int quadrant 1.")
	}

	p2 := Point{-200, 10}
	q2 := p2.Quadrant()
	if q2 != 2 {
		t.Error("p2 is not int quadrant 2.")
	}

	p3 := Point{-111, -333}
	q3 := p3.Quadrant()
	if q3 != 3 {
		t.Error("p3 is not int quadrant 3.")
	}

	p4 := Point{3, -20}
	q4 := p4.Quadrant()
	if q4 != 4 {
		t.Error("p4 is not int quadrant 4.")
	}

	p5 := Point{}
	if p5.x != 0 || p5.y != 0 {
		t.Error("Empty point must have coordinates (0, 0).")
	}
	q5 := p5.Quadrant()
	if q5 != 1 {
		t.Error("p5 (0,0) and it must be in quadrant 1.")
	}
}

func TestQuadrangleIsInAllQuadrants(t *testing.T) {
	q1 := Quadrangle{Point{1, 1}, Point{-1, 1}, Point{-1, -1}, Point{1, -1}}
	if !q1.IsInAllQuadrants() {
		t.Error("Q1 must be in all quadrants.")
	}

	q2 := Quadrangle{Point{200, -100}, Point{-333, 128}, Point{-25, -1023}, Point{456, 71}}
	if !q2.IsInAllQuadrants() {
		t.Error("Q2 must be in all quadrants.")
	}

	var q3 = Quadrangle{Point{2, 2}, Point{3, 3}, Point{-4, 4}, Point{-5, -5}}
	if q3.IsInAllQuadrants() {
		t.Error("Q3 must not be in all quadrants.")
	}

	q4 := Quadrangle{}
	if q4.IsInAllQuadrants() {
		t.Error("Q4 is an empty quadrangle and it must not be in all quadrants.")
	}
}

func TestQuadrangleArea(t *testing.T) {
	q1 := Quadrangle{Point{1, 1}, Point{-1, 1}, Point{-1, -1}, Point{1, -1}}
	if q1.Area() != 4 {
		t.Error("Q1 must have an area of 4.")
	}

	q2 := Quadrangle{Point{2, -3}, Point{-2, 3}, Point{-3, -2}, Point{4, 1}}
	if q2.Area() != 27 {
		t.Error("Q2 must have an area of 27.")
	}
}

func TestQuadrangleIsNice(t *testing.T) {
	q1 := Quadrangle{Point{2, -3}, Point{-2, 3}, Point{-3, -2}, Point{4, 1}}

	if !q1.IsNice() {
		t.Error("Q1 is a actually a nice quadrangle.")
	}

	q2 := Quadrangle{Point{0, 1}, Point{-2, 0}, Point{0, -1}, Point{2, 0}}
	if q2.IsNice() {
		t.Error("Q2 is a actually NOT a nice quadrangle.")
	}
}
