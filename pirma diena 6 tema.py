skaicius1=10
skaicius2=5
skaicius3=1

print("---1.1---")
print(skaicius1==skaicius2)
print(skaicius2==skaicius3)
print(skaicius1>skaicius2)
print(skaicius2>skaicius3*2)
if skaicius1 % 2 == 0:
    print("lyginis")
if skaicius2 % 2 != 0:
    print("nelyginis")
if skaicius3 > 0:
    print("teigiamas")
if skaicius1 < 0:
    print("neigiamas")
if skaicius2 % 4 ==0:
    print("skaicius dalinasi is 4")
if skaicius2 % 4 !=0:
    print("skaicius nesidalina is 4")
if skaicius3 % 8 ==0:
    print("skaicius dalinasi is 8")
if skaicius3 % 8 !=0:
    print("skaicius nesidalina is 8")

print("---1.2---")
print("kiek jums metu?")
metai=int(input())
if metai >= 18:
    print("Turite teise balsuoti")
print("Nurodykite savo gautus pazymius")
pazimys1=int(input())
pazimys2=int(input())
pazimys3=int(input())
vidurkis=(pazimys1+pazimys2+pazimys3)/3
print("Pusmecio vidurkis:", vidurkis)
if vidurkis >= 0:
    print("vidurkis teigiamas")
if vidurkis >5:
    print("vidurkis yra patenkinamas")

print("---1.3---")
skaicius=6
if skaicius%5==0:
    print(skaicius*1)
    print(skaicius*2)
    print(skaicius*3)
    print(skaicius*4)
    print(skaicius*5)
if skaicius %2 ==0:
    print(skaicius)
    kvadratas=skaicius*2
    print(kvadratas)
    dalyba=kvadratas/2
    print(dalyba)
if skaicius %7!=0:
    print("iveskite skaiciu")
    skaicius1=int(input())
    print(skaicius+skaicius1)
    print(skaicius-skaicius1)
    print(skaicius*skaicius1)
    print(skaicius/skaicius1)

print("---1.4---")
kintamasis1=2
kintamasis2=4
kintamasis3=8
if kintamasis1>kintamasis2:
    print("pirmas didesnis uz antra")
elif kintamasis2>kintamasis3:
    print("antras didesnis uz trecia")
elif kintamasis3>kintamasis1:
    print ("trecias didesnis uz pirma")

kintamasis1=2
kintamasis2=4
kintamasis3=8
if kintamasis1 == kintamasis2:
    print("pirmas ir antras lygus")
elif kintamasis2 == kintamasis3:
    print("antras ir trecias lygus")
elif kintamasis1 == 0:
    print("pirmas lygus nuliui")
elif kintamasis2 < 0:
    print("antras yra neigiamas")
elif kintamasis3 > 0:
    print("trecias yra teigiamas")

egzamino_pazimys = 7
if egzamino_pazimys ==10:
    print("puiku")
elif egzamino_pazimys >=9:
    print("labai gerai")
elif egzamino_pazimys >=7:
    print("gerai")
elif egzamino_pazimys >=5:
    print("patenkinamai")
elif egzamino_pazimys <5:
    print("egzaminas neislaikytas")

print("---1.5---")
print("iveskite skaiciu nuo 1 iki 100")
jusu_skaicius=int(input())
if jusu_skaicius % 2 ==0:
    print("skaicius yra lyginis")
else:
    print("skaicius yra nelyginis")

print("iveskite skaiciu nuo 1 iki 100")
jusu_skaicius=int(input())
if jusu_skaicius % 7 ==0:
    print("skaicius dalinasi is septyniu")
else:
    print("skaicius nesidalina is septyniu")

failas = 'failai/paskaitos/uzrasai.py'
if failas.endswith(".py"):
    print("tai programavimo failas")
else:
    print("nezinomas failas")

print("---1.6---")
skaicius = 20
if skaicius % 2 == 0:
    print("skaicius yra lyginis")
elif skaicius % 5 == 0:
    print("skaicius dalinasi is penkiu")
elif skaicius == 3:
    print("skaicius lygus 3")
else:
    print("klaidingas skaicius")

skaicius1=15
skaicius2=21
skaicius3=4
if skaicius1 == skaicius2:
    print("pirmi skaiciai lygus")
elif skaicius1 == skaicius3:
    print("pirmas ir trecias skaiciai lygus")
elif skaicius3 > skaicius1:
    print("trecias didesnis uz pirma")
elif skaicius2 == skaicius3*2:
    print("antras lygus dvigubam treciam")
elif skaicius1 % 3 == 0:
    print("pirmas dalinasi is 3")
else:
    print("klaidingas pasirinkimas")

print("---1.7---")
print("Iveskite tris skaicius")
skaicius1=int(input())
skaicius2=int(input())
skaicius3=int(input())
if skaicius1 > skaicius2 and skaicius1 > skaicius3:
    print("pirmas skaicius didziausias")
elif skaicius2 > skaicius1 and skaicius2 > skaicius3:
    print("antras skaicius didziausias")
else:
    print("trecias skaicius yra didziausias")

print("Iveskite tris skaicius")
skaicius1=int(input())
skaicius2=int(input())
skaicius3=int(input())
if skaicius1 < skaicius2 and skaicius1 < skaicius3:
    print("pirmas skaicius maziausias")
elif skaicius2 < skaicius1 and skaicius2 < skaicius3:
    print("antras skaicius maziausias")
else:
    print("trecias skaicius yra maziausias")

print("Iveskite pazymius nuo 1 iki 10")
skaicius1=int(input())
skaicius2=int(input())
skaicius3=int(input())
vidurkis = (skaicius1 + skaicius2 + skaicius3) / 3
print("vidurkis:",vidurkis)
if vidurkis >= 8 and vidurkis <= 10:
    print("vidurkis patenka tarp 8 ir 10")
elif vidurkis >= 5 and vidurkis <= 8:
    print("vidurkis patenka tarp 5 ir 8")
else:
    print("vidurkis maziau 5")

numeris1=20
numeris2=33
if numeris1 > numeris2 or numeris1 ==0:
    print("true 1 salyga")
if numeris2 > numeris1 or numeris2 ==5:
    print("true 2 salyga")
if numeris1 > numeris2 and numeris1 ==20:
    print("true 3 salyga")
if numeris2 > numeris1 and numeris2 <100:
    print("true 4 salyga")

