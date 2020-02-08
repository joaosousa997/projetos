def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 != 0:
        return 3*number+1


try:
    n = int(input('Enter a number: \n'))
    while n != 1:
        n = collatz(n)
        print(int(n))
except ValueError:
    print('Please insert only integers')
