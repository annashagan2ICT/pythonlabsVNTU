n = int(input("Number:"))


for num in range(10, 100):
    first_digit = num // 10  
    second_digit = num % 10   
    
   
    sum_sq = first_digit**2 + second_digit**2
    
   
    if sum_sq % n == 0:
        print(num, end=" ")