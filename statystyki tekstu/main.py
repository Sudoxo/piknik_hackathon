f = open("sample-text-file.txt", "r")
text = f.read()

print("Liczba znaków:", len(text))
print("Liczba słów:", len(text.split(" ")))
print("Liczba wierszy:", text.count("\n")+1)
while(True):
    c = input("Wprowadź znak lub słowo, którego ilość wystąpień chcesz policzyć: ")
    print(text.count(c))
    yn = input("Czy chcesz sprawdzić inny znak/słowo? (y/n) ")
    if(yn == 'n'):
        break
    
