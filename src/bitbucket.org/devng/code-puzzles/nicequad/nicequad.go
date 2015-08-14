// Full source code is available @ https://bitbucket.org/devng/code-puzzles
// Author Nikolay Georgiev, devng.com
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

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

// Quadrant gets the quadrant for a point.
// Returns 1 (where the signs of the two coordinates are (+,+)), 2 (−,+), 3 (−,−), and 4 (+,−).
// Note 0 is considered to have a + sign
func (p *Point) Quadrant() int {
	if p.x >= 0 && p.y >= 0 {
		return 1
	} else if p.x < 0 && p.y >= 0 {
		return 2
	} else if p.x < 0 && p.y < 0 {
		return 3
	}
	return 4
}

// IsInAllQuadrants checks if the quadrange has a point in all 4 quadrants
func (q *Quadrangle) IsInAllQuadrants() bool {
	quadrants := new([4]bool)
	points := [4]Point{q.a, q.b, q.c, q.d}

	for _, p := range points {
		quadrants[p.Quadrant()-1] = true
	}

	for _, b := range quadrants {
		if !b {
			return false
		}
	}

	return true
}

// Area implements Green's theorem, also known as the shoelace theorem
// or the surveyors' theorem, which is the 2D case of the more general Stokes' theorem.
// Call this function only if inAllQuadrants() returns true.
// See http://code.activestate.com/recipes/578275-2d-polygon-area/
// See http://www.mathpages.com/home/kmath201/kmath201.htm
// See https://en.wikipedia.org/wiki/Shoelace_formula
func (q *Quadrangle) Area() float64 {
	// use this array to order the points by quadrant
	orderedPoints := new([4]Point)
	for _, p := range [4]Point{q.a, q.b, q.c, q.d} {
		orderedPoints[p.Quadrant()-1] = p
	}

	// calculate the area using the Green's theorem
	total := 0
	for i, p := range orderedPoints {
		v1 := p
		v2 := orderedPoints[(i+1)%4]
		total += v1.x*v2.y - v1.y*v2.x
	}

	return math.Abs(float64(total) / 2.0)
}

// IsNice returns true if the quadrangle has points in all 4 quadrants and its area is an integer
func (q *Quadrangle) IsNice() bool {
	if !q.IsInAllQuadrants() {
		return false
	}

	area := q.Area()

	// check if area is area is a whole number within a small epsion error
	if area-math.Trunc(area) < 0.00001 {
		return true
	}
	return false
}

// CountNiceQuadrangles counts the number of nice quadrangles in a given list of points
func CountNiceQuadrangles(points []Point) int {
	if len(points) < 4 {
		return 0
	}

	count := 0
	comb := combinations(len(points))
	for i := 0; i < len(comb); i++ {
		q := Quadrangle{points[comb[i][0]], points[comb[i][1]], points[comb[i][2]], points[comb[i][3]]}
		if q.IsNice() {
			count++
		}
	}

	return count
}

// Combinations returns 4 length subsquences of elements with a given size
// iterable.
//
// Elements are treated as unique based on their position,
// not on their value. So if the input elements are unique, there
// will be no repeat values in each combination.
//  combinations(5) -> [[1 2 3 4] [1 2 3 5] [1 2 4 5] [1 3 4 5] [2 3 4 5]]
// See https://github.com/ntns/goitertools/blob/master/itertools/itertools.go
func combinations(size int) [][]int {

	r := 4
	var iterable []int
	for i := 0; i < size; i++ {
		iterable = append(iterable, i)
	}

	pool := iterable
	n := len(pool)

	if r > n || r == 0 {
		return nil
	}

	indices := make([]int, r)
	for i := range indices {
		indices[i] = i
	}

	result := make([]int, r)
	for i, el := range indices {
		result[i] = pool[el]
	}

	results := [][]int{result}

	for {
		i := r - 1
		for ; i >= 0 && indices[i] == i+n-r; i -= 1 {
		}

		if i < 0 {
			return results
		}

		indices[i] += 1
		for j := i + 1; j < r; j += 1 {
			indices[j] = indices[j-1] + 1
		}

		result := make([]int, r)
		for i = 0; i < len(indices); i += 1 {
			result[i] = pool[indices[i]]
		}

		results = append(results, result)

	}

	return results
}

func main() {
	// The input file is passed using < to redirect the streams.
	// See https://www.codechef.com/wiki/faq_old#How_should_I_test_my_program
	scanner := bufio.NewScanner(os.Stdin)

	count := 0 // the total count of nice quadranges
	t := 0     // number of test cases
	n := 0     // number of points in the current test case
	i := -1    // file line index
	points := []Point{}
	for scanner.Scan() {
		i++
		s := scanner.Text()
		if i == 0 {
			// the first line indicates the numer of test cases
			t, _ = strconv.Atoi(s)
		} else if i == 1 {
			// the secod line is the number of points in the current test case
			n, _ = strconv.Atoi(s)
			t--
		} else {
			// the lines after the n are points
			words := strings.Fields(s)
			x, _ := strconv.Atoi(words[0])
			y, _ := strconv.Atoi(words[1])
			p := Point{x, y}
			points = append(points, p)
			n--
			if n == 0 {
				// no more points for this test case count and start a new one
				count += CountNiceQuadrangles(points)
				i = 0
				points = []Point{}
			}
		}
	}

	fmt.Println(count)
}
