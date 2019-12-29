import csv

def read_zip(fname):
    with open(fname) as f:
        data = csv.reader(f,delimiter=',')
        for row in data:
            print("insert into Zip values ("+row[0].strip()+",'"+row[1].strip()+"','"+
                  row[2].strip()+"'"+");")
            
def main():
    read_zip("zip_code_database.csv")
    
main()