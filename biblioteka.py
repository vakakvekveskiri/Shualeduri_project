

import csv

headers= ["Full_name", "Subject","Score"]
info = [
    ['giorgi gelashvili', 'matematika', '90'],
    ['giorgi gelashvili', 'kimia', '10'],
    ['gela gociridze', 'matematika', '20'],
    ['gela gociridze', 'kimia', '20']
]


with open('test.csv', 'w',newline='') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(info)


