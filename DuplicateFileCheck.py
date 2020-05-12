import hashlib;
import shutil;
from os import listdir, makedirs;
from os.path import isfile,join,isdir;

# NOTES:
# It is conversial in domains where security is of utmost importance,
# but I see it acceptable to use MD5 in this small script
# due to its lower complexity and local file hashing is not a usecase
# where security is of utmost importance. We'll also hash the results
# themselves to make search faster; walking through a list comparing
# each value is O(n^2), and we want to avoid that. A BST would also be slower,
# its complexity would be O(log n) on average.
# Each collision means a repeated file; we'll store its name and
# then move it to the output folder.
repeat = "Y";
while repeat == "Y":
    hashDict = {};
    repeatedFilesList = [];
    inputPath = input("Insert a folder to search:");
    outputPath = input("Where would you like to move the repeating files? (folder will be created if it doesn't exist):");
    try:
        if (isdir(outputPath) == False):
            makedirs(outputPath);
    except OSError:
            print("The program couldn't create the output folder.");
            exit();
            
    for f in listdir(inputPath):
        fileName = join(inputPath, f);
        if isfile(fileName):
            fileHash = hashlib.md5(open(fileName,'rb').read()).hexdigest();
            if fileHash in hashDict: # a collision; that's a repeated file!
                repeatedFilesList.append(f);
            else:
                hashDict[fileHash] = f;
                
    for f in repeatedFilesList:
        try:
            shutil.move(join(inputPath, f), join(outputPath, f));
            print("Moved: ", f, " --> ", join(outputPath, f));
        except:
            print("***Could not move: ", f);
    repeat = input("Would you like to check another folder? (Y for Yes, any key for No)").upper();
exit();
