import csv

list = [['Top Gun', 'Risky Business', 'Minority Report'], ['Titanic', 'The Revenant', 'Inception'], ['Training Day', 'Man on Fire', 'Flight']]

with open('st.cvs', 'w', newline = '') as f:
    w = csv.writer(f, delimiter=',')

    w.writerow(list[0])
    w.writerow(list[1])
    w.writerow(list[2])