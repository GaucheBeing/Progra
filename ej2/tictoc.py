num = int(input("Escribe un numero, sucio mortal!"))
if num % 15 == 0:
    print("TicToc")
elif num % 3 == 0:
    print("Tic")
elif num % 5 == 0:
    print("Toc")
else: print(num)
