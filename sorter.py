import os
if os.path.exists("sorted folder"):
     pass
else:
     os.mkdir("sorted folder")
for i in os.listdir():
    if ".png" in i:
        os.rename(i,f"sorted folder/{i}")
        os.rename(f"sorted folder/{i}",f"sorted folder/{i}")
print("All file has been moved to a seperate folder")
print(os.listdir("sorted folder"))
for i in range(len(os.listdir("sorted folder"))):
     os.rename(f"sorted folder/{os.listdir("sorted folder")[i]}",f"sorted folder/{i+1}.png")
               
