f = open("파일입출력연습.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("파일입출력연습.txt", 'r')
line = f.read()
print(line)
f.close()