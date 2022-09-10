import csv

class Database:
    def __init__(self):
        self.table = []

        self.read_csv()

    def read_csv(self):
        with open('ctg.csv', 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)

            for row in csvreader:
                self.map_row(row)

        file.close()


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
        