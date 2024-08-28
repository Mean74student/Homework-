# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]
def max(number):
    max = number[0]
    for i in range(len(number)):
        if number[i] > max:
            max = number[i]
    return max
number =[2,3,5,0,11,5,2]
print(max(number))