import csv

def read_state(fname):
    with open(fname) as f:
        data = csv.reader(f,delimiter=',')
        for row in data:
            print("insert into State values ('"+row[0].strip()+"','"+row[1].strip()+"'"+");")
            
def main():
    read_state("state_database.csv")
    
main()