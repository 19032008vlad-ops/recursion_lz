def pascal_row(n):
    if n == 0:
        return [1]
    
    prev = pascal_row(n - 1)
    
    row = [1]  
    
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i + 1])  
    
    row.append(1) 
    
    return row


def pascal_triangle(n):
    triangle = []
    for i in range(n + 1):
        triangle.append(pascal_row(i))
    return triangle


def main():
    level = int(input("Enter a level: "))
    result = pascal_triangle(level)

    for row in result:
      print(row)

if __name__ == '__main__' :
   main()
