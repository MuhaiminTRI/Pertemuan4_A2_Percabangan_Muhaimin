A=int(input("Masukkan angka: "))
B=int(input("Masukkan angka: "))
C=int(input("Masukkan angka: "))

if(A<B<C):
    print(B, "Adalah bilangan terbesar ke 2")
elif(A<C<B):
    print(C, "Adalah bilangan terbesar ke 2")
elif(C<A<B):
    print(A, "Adalah bilangan terbesar ke 2")
else:
    print("ERROR")