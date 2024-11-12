import os
#open() key function for opening files
#r read file
#a for append file
#w for write file
#x create the specified file
#t is text mode
#b is binary mode
try:
 f=open("demoFile.txt","r")# open the file with operation to
 print(f.readline())# we will read the first line in the file
 f.close()# always close the file
except:
    print("exception occured while opening the file")

try:
    #f=open("demoFileTwo.txt","x")
    f=open("demoFileTwo.txt","a")
    # either for a or w , we need to use write function to attach content to file
    f.write("this is the additional text appended to the file")
    f.close()
    #os.remove("demoFileTwo.txt")# delete file
except OSError:
    print("file already exists")

except Exception:
    print("other error")
finally:
    print("end of code")
