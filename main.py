from pyscript import document

#Non-metals
#Dictionary with information about Non-metals
#Non-metal name: non-metal details, order from non-metal, and # of non-metals

Non_metals = {
    "HYDROGEN": ("H", "Hydrogen", 1, 1.008),
    "CARBON": ("C", "Carbon", 6, 12.011),
    "NITROGEN": ("N", "Nitrogen", 7, 14.007),
    "OXYGEN": ("O", "Oxygen", 8, 15.999),
    "PHOSPHORUS": ("P", "Phosphorus", 15, 30.974),
    "SULFUR": ("S", "Sulfur", 16, 32.06),
    "SELENIUM": ("Se", "Selenium", 34, 78.971),
    "FLUORINE": ("F", "Fluorine", 9, 18.998),
    "CHLORINE": ("Cl", "Chlorine", 17, 35.45),
    "BROMINE": ("Br", "Bromine", 35, 79.904),
    "IODINE": ("I", "Iodine", 53, 126.904),
    "NEON": ("Ne", "Neon", 10, 20.180),
    "ARGON": ("Ar", "Argon", 18, 39.948),
    "HELIUM": ("He", "Helium", 2, 4.003),
    "KRYPTON": ("Kr", "Krypton", 36, 83.798),
    "XENON": ("Xe", "Xenon", 54, 131.293),
    "RADON": ("Rn", "Radon", 86, 222),
}

#create a function to search a non-metal element in the dictionary

def search_element(e):
    #get the input value from HTML
    Element1 = document.getElementById("nonmetal1").value
    #retrieve information from the dictionary
    result = Non_metals.get(Element1, ("Element not found", "-", "-", "-"))
    #display the result
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("order").innerText = result[2]
    document.getElementById("count").innerText = result[3]

 
