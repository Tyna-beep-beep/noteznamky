cislo=[2,4,5,6]
hodnota = int(input("zadejte cislo"))
for i in range(4):
    if hodnota==cislo[i]:
        print(f"cislo je v poli",i)
    else:
        print("cislo není v poli")