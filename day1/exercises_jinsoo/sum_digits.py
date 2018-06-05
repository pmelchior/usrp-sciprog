import sys

def sum_digits(num):
    x = 0
    while num:
        x += num % 10
        num //= 10
    return x

if (len(sys.argv)==2):
    multiplier = 1
    while (multiplier*int(sys.argv[1]) <= int(sys.argv[1])**2):
        print(sum_digits(int(sys.argv[1])*multiplier))
        multiplier += 1

elif (len(sys.argv)==3):
    multiplier = 1
    while (multiplier*int(sys.argv[1]) <= int(sys.argv[2])):
        print(sum_digits(int(sys.argv[1])*multiplier))
        multiplier += 1

else:
    raise ValueError('Too many or too little inputs')
