import csv
from operator import itemgetter

class Database:
    def __init__(self):
        self.table = []
        self.table_sorted = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

        self.read_csv()
        self.sort_table()

    def read_csv(self):
        with open('ctg.csv', 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)

            for row in csvreader:
                self.map_row(row)

    def map_row(self, row):
        x_in = []
        for i in range(0, 21):
            if(row[i]):
                num = float(row[i])
                x_in.append(num)

        y = []
        for i in range(21, 31):
            if(row[i]):
                num = int(row[i])
                y.append(num)
        
        self.table.append([x_in, y])
        
    def sort_table(self):
        for line in self.table:
            for i in range(len(line[1])):
                if(line[1][i] == 1):
                    self.table_sorted[i].append(line)
                    break
        