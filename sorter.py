import os

if os.path.exists("sorted folder"):
     pass
else:
     os.mkdir("sorted folder")
file_name=input("enter your file type which you want to sort: ")
if "." in file_name:
    for i in os.listdir():
        if file_name in i:
            os.rename(i,f"sorted folder/{i}")
            #os.rename(f"sorted folder/{i}",f"sorted folder/{i}{file_name}")
    print("All file has been moved to a seperate folder")
    print(os.listdir("sorted folder"))
else:
     print("Please enter correct file name")

for i in range(len(os.listdir("sorted folder"))):
     os.rename(f"sorted folder/{os.listdir("sorted folder")[i]}",f"sorted folder/{i+1}{file_name}")