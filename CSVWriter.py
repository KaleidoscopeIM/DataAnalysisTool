import csv


class CSVWrite:
    def __init__(self, filename):
        self.filename = './'+filename
        self.create_header()

    def create_header(self):
        with open(self.filename, 'w', newline='') as result_file:
            result_file.truncate()
            result_writer = csv.writer(result_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            headers = ['CRASH_YEAR', 'STATE', 'ST_CASE', 'VEHICLE_BODY_TYPE', 'VIN', 'MODEL_YEAR', 'MOTORCYCLE_BODY_TYPE']
            result_writer.writerow(headers)
            result_file.flush()
            print("File created >>> " + self.filename)

    def write_data(self, row):
        with open(self.filename, 'a', newline='') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            result_writer.writerow(row)
            result_file.flush()
            print("Data inserted >>> ")
            print(row)