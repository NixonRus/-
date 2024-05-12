journal = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = list(students)
students_.sort()

for i in range(len(students_)):
    journal[students_[i]] = sum(grades[i]) / len(grades[i])

print(journal)



sr_chek = {}
table = ['1', '2', '3', '4', '5', '6', '7']
chek = [[700, 820, 480, 530, 1200], [950, 710, 630, 400, 870], [300, 710, 560, 1500], [300, 270, 1100, 800, 730, 550],
        [230, 620, 470, 980, 770], [1300, 420, 590, 710, 220], [350, 480, 510, 900, 270, 100]]

for i in range(len(table)):
    sr_chek[table[i]] = sum(chek[i]) / len(chek[i])

print(sr_chek)

list_sr_chek = sr_chek.values()
print(list_sr_chek)

sr_chek_global = sum(list_sr_chek) / len(list_sr_chek)
print(sr_chek_global)