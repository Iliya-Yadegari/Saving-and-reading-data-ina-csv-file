import csv

def get_2():
        fields = ['name','age','phone number']
        
        
        with open('test.csv','a') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            csvwriter.writerow(fields)
