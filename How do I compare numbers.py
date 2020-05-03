x = 41
def what_is(x):
    if x == 42:
        return 'everything'
    if x == 42*42:
        return 'everything squared'
    else:
        return 'nothing'
wynik = what_is(x)
print(wynik)