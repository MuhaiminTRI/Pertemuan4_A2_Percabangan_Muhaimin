N=input("Pemain A,B:")
N=N.split()

if N[0] == "[]" and N[1] == "8<":
    print(N)
    print("Pemain B Menang")
elif N[0] == "()" and N[1] == "8<":
    print(N)
    print("Pemain A Menang")
elif N[0] == "()" and N[1] == "()":
    print(N)
    print("Draw")
elif N[0] == "()" and N[1] == "()":
    print(N)
    print("Draw")
elif N[0] == "[]" and N[1] == "[]":
    print(N)
    print("Draw")
elif N[0] == "8<" and N[1] == "8<":
    print(N)
    print("Draw")
else:
    print("None")