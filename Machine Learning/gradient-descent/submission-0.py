class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for iteration in range(iterations):
            gradient = 2 * x
            x = x - (gradient * learning_rate)
            print(f"Iteration {i+1}: x = {x}, f(x) = {x**2}")

        return round(x, 5) 