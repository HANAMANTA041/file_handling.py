#Ex:Writing multiple lines to a file
f = open("PES_data.txt",'a')
list = ["Python\n","HTML\n","Javascript\n","Data Science"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()



