print("---1.1---")
print("iveskite savo varda")
vardas=input()
print("kiek jums metu?")
metai=input()
print("kodel pasirinkote kursus?")
priezastis=input()
print(f"{vardas} ({metai}m.) pasirinko mokintis, nes {priezastis}.")

print("---1.2---")
print("iveskite norima simboli")
simbolis=input()
print(simbolis, simbolis)
print(simbolis, simbolis)

print("---1.3---")
print("iveskite norima simboli")
simbolis1=input()
print(simbolis1)
print(simbolis1, simbolis1)
print(simbolis1, simbolis1, simbolis1)

print("---1.4---")
print("Koks jusu vardas")
vardas=(input())
print("Kiek jums metu?")
metai=int(input())
print("Koks jusu ugis?")
ugis=float(input())
print("Ivesta asmens informacija:")
print(vardas, type(vardas))
print(metai, type(metai))
print(ugis, type(ugis))

print("---1.5---")
print("Nurodykite savo gautus pazymius")
pazimys1=int(input())
pazimys2=int(input())
pazimys3=int(input())
pazimys4=int(input())
pazimys5=int(input())
vidurkis=(pazimys1+pazimys2+pazimys3+pazimys4+pazimys5)/5
print("Pusmecio vidurkis:", vidurkis)

print("---1.6---")
print("prasome nurodykite nueitus metrus")
metrai=int(input())
centimetrai=metrai*100
milimetrai=centimetrai*100
kilometrai=metrai/1000
print("atstumas centimetrais:",centimetrai)
print("atstumas milimetrais", milimetrai)
print("atstumas kilometrais", kilometrai)

print("---1.7---")
print("Iveskite du sveikuosius skaicius")
skaicius1=int(input())
skaicius2=int(input())
suma=skaicius1+skaicius2
skirtumas=skaicius1-skaicius2
sandauga=skaicius1*skaicius2
dalmuo=skaicius1/skaicius2
print("Suma:",suma)
print("Skirtumas:",skirtumas)
print("sandauga:", sandauga)
print("Dalmuo:", dalmuo)

print("---1.8---")
print("Iveskite du sveikuosius skaicius")
skaicius1=int(input())
skaicius2=int(input())
dalybos_liekana=skaicius1%skaicius2
print("Liekana po dalybos:",dalybos_liekana)

print("---1.9---")
print("Iveskite du sveikuosius skaicius")
skaicius1=int(input())
skaicius2=int(input())
kelimas1=skaicius1**skaicius2
kelimas2=skaicius2**skaicius1
print(kelimas1)
print(kelimas2)