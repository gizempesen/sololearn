myfile = open("filename.txt")
#-----------------------------------
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
#-----------------------------------
file = open("filename.txt", "w")
# do stuff to the file
file.close()
#-----------------------------------
#Read

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
#-----------------------------------
file = open("filename.txt", "r")

for line in file:
    print(line)

file.close() 

#Line 1 text
#Line 2 text
#Line 3 text
#-----------------------------------
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

#This has been written to a file
#-----------------------------------





