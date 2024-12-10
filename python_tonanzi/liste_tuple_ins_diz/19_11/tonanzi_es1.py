nations = ["ungheria", "mississippi", "italia", "namibia"]
capitaly = ["budapest", "jackson", "roma", "windhoek"]


ricerca = str(input("inserire nazione:"))

for naz in range(len(nations)):
    if nations[naz].lower() == ricerca.lower():
        print(f"capitale: {capitaly[naz]}")
    else:
        print("errore")