# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum(number):
    sum = 0
    for i in range(len(number)):
        if number[i] % 2 != 0:
            sum += number[i]
    return sum
number = [1,2,3,4,5,6]
print(sum(number))