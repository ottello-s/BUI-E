dichte = {"Beton": 2400, "Stahl" : 7850, "Holz": 500}

print(dichte["Beton"])
""" print(dichte-get("Glas"))
 """
dichte["Holz"] = 350

dichte["Glas"] = 2500

print("Beton" in dichte)

for baustoff.wert in dichte.items():
    print(f"{baustoff}: {wert} kg/m3")
