num = int(input())
bonus = 0

if num <= 100:
    bonus = num
    if bonus % 2 == 0:
        bonus += 1 + 5
    elif bonus % 5 == 0:
        bonus += 2 + 5
    else:
        bonus = num+5

elif num <= 1000:
    bonus = num
    if bonus % 2 == 0:
        bonus += 1 + (num * 0.20)
    elif bonus % 10 == 5:
        bonus += 2 + (num * 0.20)
    else:
        bonus = num+(num * 0.20)
else:
    bonus = num
    if bonus % 2 == 0:
        bonus += 1 + (num * 0.10)
    elif bonus % 10 == 5:
        bonus += 2 + (num * 0.10)
    else:
        bonus = num+(num * 0.10)

print("%.1f" % (bonus - num))
print("%.1f" % bonus)
