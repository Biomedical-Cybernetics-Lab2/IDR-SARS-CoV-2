from urllib import request
import pandas as pd
import re

df1 = pd.read_csv("./docking-summary/simple.csv")
df2 = pd.read_csv("./docking-summary/modeller-best.csv")
df3 = pd.read_csv("./docking-summary/modeller-avg.csv")

table1 = []
table2 = []
table3 = []

index = 1

for molecule in df1['Molecule'][0:100]:
    print('Processing molecule', index)

    link = "https://dtp.cancer.gov/dtpstandard/servlet/ChemData?outputformat=html&searchtype=NSC&searchlist="
    link += str(molecule)

    resp = request.urlopen(link)

    data = resp.read()

    html = data.decode('UTF-8')

    #print(html)

    names = re.findall(r'<LI>.+', html)

    if len(names) > 0:
        if len(names) > 6:
            names = names[0:6]
        cur = []
        cur.append(molecule)
        for name in names:
            cur.append(name[4:-1])

        table1.append(cur)

    index += 1

index = 1

for molecule in df2['Molecule'][0:100]:
    print('Processing molecule', index)

    link = "https://dtp.cancer.gov/dtpstandard/servlet/ChemData?outputformat=html&searchtype=NSC&searchlist="
    link += str(molecule)

    resp = request.urlopen(link)

    data = resp.read()

    html = data.decode('UTF-8')

    #print(html)

    names = re.findall(r'<LI>.+', html)

    if len(names) > 0:
        if len(names) > 6:
            names = names[0:6]
        cur = []
        cur.append(molecule)
        for name in names:
            cur.append(name[4:-1])

        table2.append(cur)

    index += 1

index = 1

for molecule in df3['Molecule'][0:100]:
    print('Processing molecule', index)

    link = "https://dtp.cancer.gov/dtpstandard/servlet/ChemData?outputformat=html&searchtype=NSC&searchlist="
    link += str(molecule)

    resp = request.urlopen(link)

    data = resp.read()

    html = data.decode('UTF-8')

    #print(html)

    names = re.findall(r'<LI>.+', html)

    if len(names) > 0:
        if len(names) > 6:
            names = names[0:6]
        cur = []
        cur.append(molecule)
        for name in names:
            cur.append(name[4:-1])

        table3.append(cur)

    index += 1

results1 = pd.DataFrame(table1, columns=['Molecule','Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6'])
results2 = pd.DataFrame(table2, columns=['Molecule','Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6'])
results3 = pd.DataFrame(table3, columns=['Molecule','Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6'])

results1.to_csv(r'./molecule-names/simple.csv', index = False, header=True)
results2.to_csv(r'./molecule-names/modeller-best.csv', index = False, header=True)
results3.to_csv(r'./molecule-names/modeller-avg.csv', index = False, header=True)