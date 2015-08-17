package main

import "testing"

func TestCountSundays(t *testing.T) {
  sundays := CountSundays(2015, 2016)
  if sundays != 3 {
    t.Error("Sundays should be 3.")
  }

  sundays = CountSundays(1901, 2001)
  if sundays != 171 {
    t.Error("Syndays should be 171.")
  }
}
