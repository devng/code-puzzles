package nicequad

import (
	"testing"
)

func TestPointQuadrant(t *testing.T) {
	p1 := Point{1, 1}
	q1 := p1.quadrant()
	if q1 != 1 {
		t.Error("p1 is not int quadrant 1.")
	}

	p2 := Point{-200, 10}
	q2 := p2.quadrant()
	if q2 != 2 {
		t.Error("p2 is not int quadrant 2.")
	}

	p3 := Point{-111, -333}
	q3 := p3.quadrant()
	if q3 != 3 {
		t.Error("p3 is not int quadrant 3.")
	}

	p4 := Point{3, -20}
	q4 := p4.quadrant()
	if q4 != 4 {
		t.Error("p4 is not int quadrant 4.")
	}

	p5 := Point{}
	if p5.x != 0 || p5.y != 0 {
		t.Error("Empty point must have coordinates (0, 0).")
	}
	q5 := p5.quadrant()
	if q5 != 1 {
		t.Error("p5 (0,0) and it must be in quadrant 1.")
	}
}

func TestQuadrangleInAllQuadrants(t *testing.T) {
	q1 := Quadrangle{Point{1, 1}, Point{-1, 1}, Point{-1, -1}, Point{1, -1}}
	if !q1.inAllQuadrants() {
		t.Error("Q1 must be in all quadrants.")
	}

	q2 := Quadrangle{Point{200, -100}, Point{-333, 128}, Point{-25, -1023}, Point{456, 71}}
	if !q2.inAllQuadrants() {
		t.Error("Q2 must be in all quadrants.")
	}

	var q3 = Quadrangle{Point{2, 2}, Point{3, 3}, Point{-4, 4}, Point{-5, -5}}
	if q3.inAllQuadrants() {
		t.Error("Q3 must not be in all quadrants.")
	}

	q4 := Quadrangle{}
	if q4.inAllQuadrants() {
		t.Error("Q4 is an empty quadrangle and it must not be in all quadrants.")
	}
}
