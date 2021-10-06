def print_meniu():
    print("1. Determina daca un numar e palindrom")
    print("2. Ultimul nr prim mai mic decat un numar dat")
    print("3. Calculeaza combinari de n luate cate k")
    print("4. Iesire")

def prim(p):
    if p<2:
        return False
    else:
        for i in range(2,p//2+1):
            if p%i==0:
                return False
    return True

def get_largest_prime_below(n):
    i=n-1
    ok=0
    while i>1 and ok==0:
        if prim(i)==1:
            ok=1
            return i
        else:
            i=i-1

def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(20) == 19

def oglindit(n):
    nr=0
    while n!=0:
        nr=nr*10+n%10
        n=n//10
    return nr

def is_palindrome(n):
    if n==oglindit(n):
        return True
    return False

def test_is_palindrome():
    assert is_palindrome(5)==True
    assert is_palindrome(12)==False
    assert is_palindrome(12321)==True

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def test_factorial():

    assert factorial(5)==120

def get_n_choose_k(n, k):
    n1=factorial(n)
    n2=factorial(k)
    n3=factorial(n-k)
    numitor=n2*n3
    return n1//numitor

def test_get_n_choose_k():
    assert get_n_choose_k(10,2)==45
    assert get_n_choose_k(15,10)==3003

def main():
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            numar=int(input("Dati numarul:"))
            if is_palindrome(numar)==1:
                print("E palindrom")
            else:
                print("Nu e palindrom")
        elif option == 2:
            nr=int(input("Dati numarul:"))
            rez=get_largest_prime_below(nr)
            print(rez)
        elif option==3:
            n=int(input("Dati n:"))
            k = int(input("Dati k:"))
            rezultat=get_n_choose_k(n,k)
            print(rezultat)
        elif option == 4:
            break
        else:
            print("optiune invalida ! Reincercati !")
    test_is_palindrome()
    test_factorial()
    test_get_n_choose_k()
    test_get_largest_prime_below()
if __name__ == '__main__':
    main()
