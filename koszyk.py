import pprint

def main():

    produkt_1 = {'nazwa': 'mlekovita',
                'cena': '10',
                'vat': '7',
                'jednostka': '5'}

    produkt_2 = {'nazwa': 'ziemniaki',
                'cena': '5',
                'vat': '23',
                'jednostka': '8'}

    produkt_3 = {'nazwa': 'pomidory',
                'cena': '12',
                'vat': '23',
                'jednostka': '18'}

    koszyk = [produkt_1, produkt_2, produkt_3]

    file = open("koszyk.csv", "w")
    for poz in koszyk:
        for pole in ['nazwa', 'cena', 'vat', 'jednostka']:
            file.write("{0},".format(poz[pole]))
        file.write("\n")
    file.close()

        
    koszyk2 = []
    print("### koszyk2")

    file2 = open("koszyk.csv", "r")
    calosc = file2.read()
    linie = calosc.split('\n')
    for l in linie:
        produkt = {}
        if len(l) > 0:
            pola = l.split(',')
            produkt['nazwa'] = pola[0]
            produkt['cena'] = pola[1]
            produkt['vat'] = pola[2]
            produkt['jednostka'] = pola[3]
            koszyk2.append(produkt)

        pprint.pprint(produkt)
    
if __name__ == "__main__":
     main()
