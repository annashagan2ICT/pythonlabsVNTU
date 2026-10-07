d = float(input())
t = float(input())

days = 1             
total_dist = d       
current_day = d      

while total_dist <= t:
    days += 1
    current_day *= 1.10       
    total_dist += current_day

print(f"{total_dist:.2f} km, {days} days")