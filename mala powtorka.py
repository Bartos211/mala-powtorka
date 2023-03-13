name = "Lista zakupow"
print(name)
dict= {
"Piekarnia":["Chleb","Pączek","Bułki"],
"Warzywniak":["Marchew","Seler","Rukola"]
}

shop1 = "Piekarnia"
shop2 = "Warzywniak"
products1 = "Chleb","Pączek","Bułki"
products2 = "Marchew","Seler","Rukola"
shops = f"Idę do {shop1},kupuje tam {products1}"
f"Idę do {shop2},kupuje tam{products2}"


for klucz,wartość in dict.items():
    print(shops)
    
stores= ['Chleb','Pączek','Bułki','Marchew','Seler','Rukola']
print(len(stores))
print('W sumie kupuje 6 produktow')