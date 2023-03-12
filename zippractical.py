import glob
import zipfile

# Creating A Zip Object
zipobj = zipfile.ZipFile('combo.zip', 'w', zipfile.ZIP_DEFLATED)

# Getting All the txt files with glob.glob() functions
for i in glob.glob('*.txt'): # iterating on every txt file in cwd instead of adding them one by one
    zipobj.write(i)     # zipping the files
zipobj.close()  # must close Zipobj otherwise, it will conflict wth extract function

# extracting Data:
zipfiles = zipfile.ZipFile('combo.zip' , 'r')
zipfiles.printdir()  # listing all the files present in archive
zipfiles.extractall('extracted_data')
print('\nArchive Decompressed Successfully')
zipfiles.close()   # Always Close the fileobj when the work is done.
print('\033[1;92mCoded by Durani Mohammed Zaeem: Roll no: 425\033[0m')

# Source code originally belongs to © Zaeem Durani 