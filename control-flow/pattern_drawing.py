pattern_size = int(input("Enter the size of the pattern: "))
number = 0
while number < pattern_size :
    for y in range(0, pattern_size):
        print('*' ,end='')
    print()
    number += 1
