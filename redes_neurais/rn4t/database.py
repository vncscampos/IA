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
        parsed_row = []
        for i in range(0, 21):
            if(row[i]):
                num = float(row[i])
                parsed_row.append(num)

        for i in range(21, 31):
            if(row[i]):
                num = int(row[i])
                parsed_row.append(num)
        
        self.table.append(parsed_row)