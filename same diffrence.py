t = int(input())


for i in range(t):
    
    n = int(input())
  
    s = input()
    
   
    last_char = s[-1]
    
    operations = 0
    
    for char in s:
        # If the character does not match the last one, we must change it
        if char != last_char:
            operations += 1
            
    print(operations)