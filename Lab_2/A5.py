# A5: делится ли A на B нацело, без ветвлений
a = int(input())
b = int(input())
print(["NO", "YES"][a % b == 0])
