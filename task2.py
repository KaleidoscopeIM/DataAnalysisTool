import csv
import requests
from CSVWriter import CSVWrite
from Utility import *
output_file = 'result_shilpi.csv'
file_writer = CSVWrite(output_file)
crash_year = 2016


# sample API url =  https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/5UXWX7C5*BA?format=csv&modelyear=2011
def start_fetch_process(csv_file):
    with open(csv_file, 'r') as vehicle_csv:
        dict_reader = csv.DictReader(vehicle_csv)

        for aRow in dict_reader:
            state = aRow['STATE'].strip()
            st_case = aRow['ST_CASE'].strip()
            vin = 'CRF150F'  #aRow["VIN"].strip()
            mod_year = '2013'#aRow["MOD_YEAR"].strip()
            body_type = aRow["BODY_TYP"].strip()
            if state in (None, "") or st_case in (None, "") or vin in (None, "") or mod_year in (None, "") or body_type in (None, ""):
                continue
            if int(body_type) != 80:  # only want motorcycle(body type =80 in VEHICLE.csv)
                continue
            print('--------------------------------')
            print("st_case >>"+st_case+"  VIN >> " + vin + '  mod_year >> ' + mod_year + "   body_type >> " + body_type)
            url = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/" + vin + "?format=csv&modelyear=" + mod_year
            response = requests.get(url)
            if response.status_code != 200:
                print("failed to get data from url: " + url)
            else:
                reader = csv.DictReader(response.text.strip().split('\n'))
                record = next(reader)
                bodyclass = record["bodyclass"]
                if body_type in (None,""):
                    continue
                print("bodyclass >> "+bodyclass)
                row = []
                row.append(crash_year)
                row.append(state)
                row.append(st_case)
                row.append(body_type)
                row.append(vin)
                row.append(mod_year)
                row.append(bodyclass)
                file_writer.write_data(row)


while True:
    vehicle_csv_file = get_vehicle_csv_of(crash_year)
    start_fetch_process(vehicle_csv_file)
    crash_year = crash_year+1
    if crash_year == 2019:  # start year = 2016 and end year =2018
        print("Process completed.")
        break




