import bs4 as bs
import lxml
import urllib.request
import csv
sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Albury.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('albury.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)
sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/BadgerysCreek.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('badgery.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)
sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Cobar.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('cobar.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)
sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/CoffsHarbour.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('coffs.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)
sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Moree.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('moore.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Newcastle.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('newcastle.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/NorahHead.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('norah.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/NorfolkIsland.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('norfolk.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)


sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Penrith.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('penrith.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Richmond.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('richmond.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/Sydney.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('Sydney.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)


sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/SydneyAirport.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('SydneyAirport.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

sauce=urllib.request.urlopen("https://karki23.github.io/Weather-Data/WaggaWagga.html").read()
src=bs.BeautifulSoup(sauce,"lxml")
all=src.find_all('td')
row_data = [i.text for i in all]
i=0
new_list=[]
while i<len(row_data):
    new_list.append(row_data[i:i+24])
    i+=24
print(new_list)
with open('WaggaWagga.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Williamtown.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Williamtown.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Wollongong.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Wollongong.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Canberra.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Canberra.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Tuggeranong.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Tugger.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MountGinini.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Mountginni.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Ballarat.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Ballarat.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Bendigo.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Bendigo.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Sale.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Sale.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MelbourneAirport.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('MelbourneAir.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Melbourne.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Melbourne.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Mildura.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Mildura.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Nhil.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Nhil.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Portland.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Portland.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Watsonia.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Watsonia.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Dartmoor.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Dartmoor.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Brisbane.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Brisbane.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Cairns.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Cairns.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/GoldCoast.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('GoldCoast.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Townsville.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Townsville.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Adelaide.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Adelaide.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/MountGambier.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('MountGambier.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Nuriootpa.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Nuriootpa.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Woomera.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Woomera.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Albany.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Albany.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Witchcliffe.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Witchcliffe.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/PearceRAAF.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Pearce.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/PerthAirport.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('PerthAir.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Perth.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Perth.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/SalmonGums.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('SalmonGums.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Walpole.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Walpole.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Hobart.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Hobart.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Launceston.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Launce.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/AliceSprings.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('AliceSprings.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Darwin.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Darwin.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)

    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Katherine.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('katherine.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)


    sauce = urllib.request.urlopen("https://karki23.github.io/Weather-Data/Uluru.html").read()
    src = bs.BeautifulSoup(sauce, "lxml")
    all = src.find_all('td')
    row_data = [i.text for i in all]
    i = 0
    new_list = []
    while i < len(row_data):
        new_list.append(row_data[i:i + 24])
        i += 24
    print(new_list)
    with open('Uluru.csv', 'w+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(new_list)
csvFile.close()