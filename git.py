"""nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
total = 0
index = 0

#barcha nums ro'yhatini aylanish uchun
while index < len(nums):
    #numsni ichida juftlarini saralab olamiz 
    if nums[index] % 2 == 0:
        #yig'indisini topamiz
        total += nums[index]
    index += 1

print(total)"""

#sonlar ro'yhati
nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
#juftlarni kiritish uchun
total = 0

# Iterator yaratamiz
iterator = iter(nums)

while True:
    try:
        # Ro'yxatning elementini olamiz
        num = next(iterator)
        #agar num ro'yhatida juft sonlar bo'lsa
        if num % 2 == 0:
            #totalga numni qo'shadi
            total += num
    except StopIteration:
        # Ro'yxat tugaganida sikl to'xtaydi
        break

print(total)

#birinchi ochib olamiz write modeda nomini file deb saqlab 
with open('test.txt', 'w') as file:
    #for 100ta son generatsiya qilib beradi
    for i in range(1, 101):
        #generatsiya qilingan sonlar test.txtga yoziladi
        file.write(str(i) + '\n')
