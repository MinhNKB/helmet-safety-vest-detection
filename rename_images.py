import glob
import os
files = glob.glob("./filter-images/*")
index = 0
for file in files:
    new_file = file[ : file.rindex("\\")] + "/" + str(index).zfill(4) + ".jpg"
    index += 1
    print(file, new_file)
    os.rename(file, new_file)