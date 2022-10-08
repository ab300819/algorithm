package main

import (
	"sync"
)

type Chopstick struct {
	sync.Mutex
}

type Philosopher struct {
	name                          string
	leftChopstick, rightChopstick *Chopstick
	status                        string
}

func (p *Philosopher) dine() {

}

func main() {

}
