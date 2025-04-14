d = "hello"
for i in range(5):
    with open("file.txt", 'w', encoding="utf-8") as a:
        a1=a.write(d)
        print(a)