#GitForritunVerkefni
#Kypler Lloyd Espiritu
#25.01.17
''''
#Dæmi 1
print()
tala1 = int(input("Sláðu inn tölu 1: "))
tala2 = int(input("Sláðu inn tölu 2: "))

marg = tala1 * tala2
summ = tala1 + tala2

print("Summa talnanna er", summ)
print("Ef þú margfaldar tölurnar saman færðu",marg)

#Dæmi 2

print()
fornafn = input("Fornafn?: ")
eftirnafn = input("Eftirnafn?: ")

print("Halló",fornafn, eftirnafn)
'''
#Dæmi 3

print()
lagstaf = 0 #Lagstafir
hastaf = 0 #Hastafir
eftirha = 0 #Lagstafir eftir hastafir
minus = -1
texti = input("Sláðu inn texta: ")
leng = int(len(texti))
listi = list(texti)

for x in listi:
    if x.isupper():
        hastaf += 1
    elif x.islower():
        lagstaf += 1

for x in range(leng):
    if listi[x].islower() and listi[minus].isupper():
        minus += 1
        eftirha += 1
    else:
        minus += 1

print("Í þessum texta eru",hastaf,"hástafir,",lagstaf,"lágstafir og",eftirha,"lágstafir stra")

