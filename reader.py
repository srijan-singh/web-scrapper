import csv

def read_data(file_path):
    file = open(file_path)
    
    csvreader = csv.reader(file)
    header = next(csvreader)
    print(header)

    for row in csvreader:
        
        country = row[0] 
        asin = row[1]

        print(country, asin)

    file.close()



if __name__ == "__main__":
    
    read_data('resource\Amazon Scraping.csv')