def convert(number, base):
    digits = "0123456789ABCDEF"
    
    if number < 0:
        return "-" + convert(-number, base)
    
    if number < base:
        return digits[number]
    
    return convert(number // base, base) + digits[number % base]

def main():

    num = int(input("Enter a number: "))
    b = int(input("Enter the basis (2-16): "))

    if 2 <= b <= 16:
      print(f"{num} in system {b}: {convert(num, b)}")
    else:
      print("Try again ()")

if __name__ == '__main__' :
   main()