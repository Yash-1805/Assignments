#Task 2: Sum of Integers from 1 to 50 Using a Loop
def sum_integers():
    total = 0
    for i in range(1, 51):
        total += i
    return total
sum= sum_integers()
print(f"the sum of integers from 1 to 50 is: {sum}")