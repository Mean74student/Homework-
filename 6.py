# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]
def count_positive(number):
    count = 0
    for i in range(len(number)):
        if number[i] >= 0:
            count += 1
    return count
number = [-1,11,2,0,-1,4]
print(count_positive(number))