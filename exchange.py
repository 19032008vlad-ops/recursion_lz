def permutations(items):
    
    if len(items) <= 1:
        return [items]
    
    result = []
    
    for i in range(len(items)):
        current = items[i]
        
        rest = items[:i] + items[i+1:]
        for p in permutations(rest):
            result.append([current] + p)
    
    return result


def main():
    
    raw = input("Enter numbers through a space: ")
    
    items =[int(x) for x in raw.split()]
   
    print(f"All permutations of your numbers: {permutations(items)}") 
    

if __name__ == "__main__":
    main()
