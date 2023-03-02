package main

func main() {
	println(fib(35))
}

func fib(a int) int {
	if a < 2 {
		return 1
	}
	return fib(a-1) + fib(a-2)
}
