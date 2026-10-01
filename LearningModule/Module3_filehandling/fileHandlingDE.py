import csv
import json
import gzip
import zipfile



# basic reading and writing
def basicFileOperation():
    #writing
    print("entered main")
    with open("op1.txt", 'w') as f:
        f.write("Example of basic write \n")
        f.write("this is second line\n")
    #reading
    with open ("op1.txt",'r') as f:
        readingFileAsStr = f.read()
        print(readingFileAsStr.strip())

    #reading multiple lines , memory efficient
    with open("op1.txt","r") as f:
        for line in f:
            print(line.strip())

def csvFileOperation():
    # reading files
    with open("Social_media_impact_on_life.csv", 'r') as f:
        reader= csv.DictReader(f)
       #to print first row data
        print(next(reader)) # first data row
       # to convert the data into dict
        data= list(reader)
        #print("length of reader", len(data))
        #print(data[0]) # stored as key value pairs

        # to read only column names from csv files
        headers=reader.fieldnames
        print("headers/n", headers)
    # writing files
    with open("csv_output.csv",'w',newline='') as f:
        writer =csv.DictWriter(f, fieldnames=['id','name','age'])
        writer.writeheader()
        writer.writerow({"id": 121, 'name':'vixen','age':10})
        writer.writerow({"id": 131, 'name':'jixen','age':20})



def jsonFileOperation():
  # to load file object
    with open("colors.json",'r') as f:
        json_data=json.load(f)# reads from file object
    with open("colors_output.json",'w') as f:
        json.dump(json_data,f,indent=2)
  # to convert file object to string
    json_string=json.dumps(json_data)
    parsed=json.loads(json_string)#reads from string object
#did not test,just for understanding
def largefiles():
    with open('largefile.txt','r') as f:
        for line in f:
            process(line)

    with open('largefile.bin','rb') as fb:
        while chunk:= f.read(8000):
            process(chunk)

'''def zipfiles():
    with gzip.open('file.csv.gz','rt') as f: # rt= reat text
        content = f.read()
    with zipfile.ZipFile('archive.zip') as z:
        print(z.namelist())
        with z.open(data.csv) as f:
            content=f.read()
'''
def main():

    #basic file operations for de
    #basicFileOperation()

    #csv file operations
    #csvFileOperation()

    #json file operations
    jsonFileOperation()

    #handling large file
    largefiles()

    #zip files

if __name__ == "__main__" :
    main()