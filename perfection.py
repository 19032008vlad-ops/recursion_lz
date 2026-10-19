def sum_divisors(n, i = 1):
    
    if i > n // 2:
        return 0
    
    if n % i == 0:
        return i + sum_divisors(n, i + 1)
    else:
        return sum_divisors(n, i + 1)


def is_perfect(n):
    if n <= 1:
        return False
    return sum_divisors(n) == n


def main(): 

    number = int(input("Enter a number: "))

    if is_perfect(number):
      print("Your number is perfect")
    else:
      print("Your number isn't perfect")


if __name__ == '__main__' :
   main()