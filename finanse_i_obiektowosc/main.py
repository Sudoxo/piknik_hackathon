import csv

#use another path
#file = open(faktura.csv)
file = open('finanse_i_obiektowosc/faktura.csv', encoding='UTF8')

output = open('finanse_i_obiektowosc/output.csv', 'w', newline='', encoding='UTF8')

csvreader = csv.reader(file, delimiter=";")
writer = csv.writer(output)

header = ["NAZWA PRODUKTU","CENA NETTO", "PODATEK VAT", "NARZUT", "CENA SKLEPOWA"]
writer.writerow(header)
for row in csvreader:
    name = row[0]
    netto = int(row[1])
    vat = int(row[2])
    narzut = int(row[3])
    price = round((netto*0.01)*(1+vat*0.01)*(1+narzut*0.01),2)
    writer.writerow([name,netto,vat,narzut,price])
    
