name = "Lista zakupow"
print(name)
dict= {"Piekarnia":["Chleb","Paczek","Bulki"],
       "Warzywniak":["Marchew","Seler","Rukola"]
      }
counter = 0
for klucz,wartosc in dict.items():
    counter +=len(wartosc)
    print("Ide do {},kupuje tam rzeczy {}".format(klucz, wartosc))
print(len(wartosc))
print(counter)
print('W sumie kupuje 6 produktów')

for i in range(0,100):
        if i & 5 == 0:
            print(i)
            
for i in range(0,100):
        print(i,i**3)