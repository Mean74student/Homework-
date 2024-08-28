# EX1.Create function to sum numbers in array [1,2,3,4,5,6]
def sum(number):
    sum = 0
    for i in range(len(number)):
        sum += number[i]
    return sum
number = [1,2,3,4,5,6]
print(sum(number))