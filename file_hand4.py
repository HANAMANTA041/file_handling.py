#Ex:File management using context-manager i.e with staetement
with open("PES_data.txt","a") as f:
    f.write("pesu\n")
    f.write("Electronic\n")
    f.write("City\n")
    print("Is File Closed: ",f.closed)#False

print("Is File closed: ",f.closed)#True

#Delete a file
import os
os.remove("demofile.txt")




