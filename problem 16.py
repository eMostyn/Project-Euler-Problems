num = 2**1000
strVer = str(num)
total = 0
for i in range(0, len(strVer)):
    total += int(strVer[i])
print(total)
