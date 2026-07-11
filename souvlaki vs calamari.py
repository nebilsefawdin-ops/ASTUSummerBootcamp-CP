test_cases_string = input()
t = int(test_cases_string)

for i in range(t):
    n_string = input()
    n = int(n_string)
    
    line = input()
    string_list = line.split()
    
    numbers = []
    for item in string_list:
        number = int(item)
        numbers.append(number)
    
    numbers.sort()
    souvlaki_wins = True
    
    for index in range(1, n - 1, 2):
        if numbers[index] != numbers[index + 1]:
            souvlaki_wins = False
            
    if souvlaki_wins == True:
        print("YES")
    else:
        print("NO")