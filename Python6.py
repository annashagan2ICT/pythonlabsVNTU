a=int(input("Кількість учнів в класі №1:"))
b=int(input("Кількість учнів в класі №2:"))
c=int(input("Кількість учнів в класі №3:"))

desks_a=(a+1)//2
desks_b=(b+1)//2
desks_c=(c+1)//2

desks=desks_a + desks_b + desks_c

print(f"Найменша можлива кількість парт:{desks}")