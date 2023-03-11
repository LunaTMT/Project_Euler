numbers = [i for i in range(1, 101)]

sum_of_squares = sum(map(lambda x: x ** 2, numbers))

square_of_sum = sum(numbers) ** 2

diff = square_of_sum - sum_of_squares
print(diff)