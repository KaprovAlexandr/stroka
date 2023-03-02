N = input("Введите кол-во слов: ")
spisok = []
for i in range(int(N)):
    spisok.append(input())
    print(spisok)
str = ' '.join(spisok)
print(str)
