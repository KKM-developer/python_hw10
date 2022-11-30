class MinStat:

    def __init__(self):
        self.number_list = []

    def add_number(self,number):
        self.number_list.append(number)

    def result(self):
        try:
            return min(self.number_list)
        except:
            return None

class MaxStat:

    def __init__(self):
        self.number_list = []

    def add_number(self, number):
        self.number_list.append(number)

    def result(self):
        try:
            return max(self.number_list)
        except:
            return None

class AverageStat:

    def __init__(self):
        self.number_list = []

    def add_number(self, number):
        self.number_list.append(number)

    def result(self):
        try:
            return sum(self.number_list) / len(self.number_list)
        except:
            return None

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

class Table:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.main_table = []
        for r in range(rows):
            r = []
            for c in range(cols):
                r.append(0)
            self.main_table.append(r)

    def get_value(self, row, col):
        try:
            return self.main_table[row][col]
        except:
            return None

    def set_value(self, row, col, val):
        self.main_table[row][col] = val

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.main_table.pop(row)

    def delete_col(self, col):
        for r in range(self.rows):
            self.main_table[r].pop(col)

    def add_row(self, row):
        self.main_table.insert(row, [x*0 for x in range(self.cols)])
        # for i in range(self.cols):
        #     self.main_table[row].append(0)

    def add_col(self, col):
        for i in range(self.rows):
            self.main_table[i].insert(col, 0)


# Задача 2.
# Пример 1.
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

# Пример 2.
tab = Table(2, 2)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_col(1)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
#
# Пример 3.
tab = Table(1, 1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()
