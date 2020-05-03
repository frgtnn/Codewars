a = [3, 5, 10]
x = 13
def check(a,x):
    if x in a:
        return True
    if x not in a:
        return False
wynik = check(a,x)
print(wynik)