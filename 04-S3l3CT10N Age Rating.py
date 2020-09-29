Age=int(input("Enter your age>>>: "))

if Age>12 and Age<15:
        print("You can watch: U,PG,12 and 12A")

elif Age>=15 and Age<18:
    print("You can watch: U,PG,12,12A and 15")

elif Age>=18:
    print("You can watch:U,PG,12,12A,15,18 and R18 (Basically you can watch all movies althogh for R18 you nedd special permision)")

else:
    print("You can watch: U and PG")
