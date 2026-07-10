t = int(input())


for i in range(t):
    
    n = int(input())
  
    s = input()
    
   
    last_char = s[-1]
    
    operations = 0
    
    for char in s:
        
        if char != last_char:
            operations += 1
            
    print(operations)