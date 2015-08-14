package nicequad

// Point with integer coordinates x and y
type Point struct {
	x int
	y int
}

// Quadrangle which consists of 4 points
type Quadrangle struct {
	a Point
	b Point
	c Point
	d Point
}

// Gets the quadrant for a point.
// Returns 1 (where the signs of the two coordinates are (+,+)), 2 (−,+), 3 (−,−), and 4 (+,−).
// Note 0 is considered to have a + sign
func (p Point) quadrant() int {
	if p.x >= 0 && p.y >= 0 {
		return 1
	} else if p.x < 0 && p.y >= 0 {
		return 2
	} else if p.x < 0 && p.y < 0 {
		return 3
	}
	return 4
}

// Checks if the quadrange has a point in all 4 quadrants
func (q Quadrangle) inAllQuadrants() bool {
	quadrants := new([4]bool)
	points := [4]Point{q.a, q.b, q.c, q.d}

	for _, p := range points {
		quadrants[p.quadrant()-1] = true
	}

	for _, b := range quadrants {
		if !b {
			return false
		}
	}

	return true
}

func (q Quadrangle) area() float64 {
	// TODO
	return 0.0
}
