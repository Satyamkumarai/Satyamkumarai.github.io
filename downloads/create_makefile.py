import os
import argparse
import sys
parser = argparse.ArgumentParser(description="Writing a makefile for all the cpp files in the current  directory")
parser.add_argument("dir",metavar="dir",help = "The directory where your cpp files are located")
parser.add_argument("-e",default="exe",metavar="extension")
parser.add_argument("-r",action ="store_true")
def Create_makefile(dir,outext = "exe",func = lambda X: X.endswith(".cpp"),recursive=False):
    """Is used to create a  makefile in the dir with executable files with extenstion outext
        func -->bool :This is the function that is used to select the files in the dir"""
    if os.path.isdir(dir):

        outext = outext.lstrip(".")

        #get all the files from the dir
        dir_ls  = os.listdir(dir)

        filesTobeProcessed= list(filter(lambda file: os.path.isfile(f"{dir}/{file}"),dir_ls))

        #get all the files that have the ext
        filesTobeProcessed = list(filter(func,filesTobeProcessed))

        #Make sure that the files list is not empty

        assert(len(filesTobeProcessed)>0)


        print("Selected Following files\n\t"+"\n\t".join(str(i[0])+". "+i[1] for i in enumerate(filesTobeProcessed,1)))
        filesWithExt = list(map(lambda x: x[:-3]+outext,filesTobeProcessed))

        print("Creating make file")

        # print(filesWithExt)
        
        #creating the make file 
        with open(dir.rstrip("/")+"/makefile","w") as mkfile:
            mkfile.write("#This make file was created by making.py\n")
            #writing the main target `all` that has all the output files as the dependencies
            mkfile.writelines("all: "+" ".join(filesWithExt)+"\n")

            # creating the output for each file..
            for inp,outp in zip(filesTobeProcessed,filesWithExt):
                mkfile.writelines(f"{outp}: {inp}\n")                
                mkfile.writelines(f"\tg++ {inp} -o {outp}\n")
            
            #make update 
            mkfile.write(f"update:\n\tpy {os.path.basename(sys.argv[0])} {dir} -e {outext}\n")
            #make clean
            mkfile.write("clean:\n\trm \"./*.exe\"")
        print("Created in "+dir.rstrip("/")+"/makefile")
        if recursive:
            dirs =  [os.path.realpath(i) for i in dir_ls if os.path.isdir(i)]
            print("Checek",dirs)
            for i in dirs:
                try:
                    Create_makefile(i,outext,func,recursive)
                except AssertionError:
                    pass
            print("done",dir)

            
if  __name__ == "__main__":
    parsed = parser.parse_args()
    dir = parsed.dir
    ext = parsed.e
    recursive= parsed.r
    # print(f"{recursive} :s")
    try:
        Create_makefile(dir,ext,recursive = recursive)
    except AssertionError:
        print(f"Sorry no files found in {dir}")



