name = "Lista zakupow"
print(name)
dict= {
        "Piekarnia":["Chleb","Paczek","Bulki"],
        "Warzywniak":["Marchew","Seler","Rukola"]
      }
for klucz,wartosc in dict.items():
    print("Ide do: {},kupuje tam rzeczy: {}".format(klucz, wartosc))
    
stores= ['Chleb','Pączek','Bułki','Marchew','Seler','Rukola']
print(len(stores))
print('W sumie kupuje 6 produktow')

for i in range(0,100):
        if i & 5 == 0:
            print(i)
            
for i in range(0,100):
        print(i,i**3)