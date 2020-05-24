import os
import glob   #to list the files
import argparse
import re
parser = argparse.ArgumentParser(description="Writing a makefile for all the cpp files in the current  directory")
parser.add_argument("dir",metavar="dir",help = "The directory where your cpp files are located")
parser.add_argument("-e",default="exe",metavar="extension")
parser.add_argument("-r",action ="store_true")

def list_files(directory, extension):
    """returns the files with certain ext in the directory"""
    saved = os.getcwd()
    os.chdir(os.path.abspath(directory))
    print(os.path.curdir)
    it = glob.glob('*.' + extension)
    os.chdir(saved)
    return it

def CreateRecusive(dir,out_ext = "exe",in_ext = "cpp",recursive=False,delcommand = "del",compiler = "g++",scriptPath=os.path.abspath(__file__)):
    for root,dirs,files in os.walk(dir):
        try:
            Create_makefile(os.path.abspath(root),out_ext = out_ext,in_ext = in_ext,recursive=False,delcommand = delcommand,compiler = compiler,scriptPath=os.path.abspath(__file__))
        except AssertionError:
            #bypassing the assertion error in recursive mode
            pass


def Create_makefile(dir,out_ext = "exe",in_ext = "cpp",recursive=False,delcommand = "del",compiler = "g++",scriptPath=os.path.abspath(__file__)):
    """Is used to create a  makefile in the dir with executable files with extenstion out_ext
        in_ext -->bool :This is the extension of the input files"""
    
    if os.path.isdir(dir):

        out_ext = out_ext.lstrip(".")
        
        if recursive:
            return CreateRecusive(dir,out_ext,in_ext,recursive,delcommand,compiler,scriptPath)
        else:
        #get all the files from the dir
            dir_ls  = os.listdir(dir)

            dir_ls = [os.path.abspath(i) for i in dir_ls]

            filesTobeProcessed= list(filter(lambda file: os.path.isfile(os.path.join(dir,file)),dir_ls))

            # filesTobeProcessed = [os.path.basename()]
            #get all the files that have the ext
            filesTobeProcessed = list_files(dir,in_ext)

            #Make sure that the files list is not empty

            assert(len(filesTobeProcessed)>0)


            print("Selected Following files\n\t"+"\n\t".join(str(i[0])+". "+i[1] for i in enumerate(filesTobeProcessed,1)))
            
            #appending ("")
            filesWithExt = list(map(lambda x: re.sub(in_ext,"$(ext)",x),filesTobeProcessed))

            print("Creating make file")

            # print(filesWithExt)
#-----------------------------------creating the make file----------------------------------------            
            #creating the make file 
            with open(os.path.join(dir,"makefile"),"w") as mkfile:

                mkfile.write("#This make file was created by making.py from https://raw.githubusercontent.com/Satyamkumarai/Satyamkumarai.github.io/master/downloads/create_makefile.py\n")

                #writing the main target `all` that has all the output files as the dependencies
                mkfile.writelines(f"ext = {out_ext}\n")
                
                mkfile.writelines("all: "+" ".join(filesWithExt)+"\n")

                # creating the output for each file..
                for inp,outp in zip(filesTobeProcessed,filesWithExt):

                    mkfile.writelines(f"{outp}: {inp}\n")                

                    mkfile.writelines(f"\t{compiler} {inp} -o {outp}\n")
                
                #make update 
                mkfile.write(f"update:\n\tpy -c \"from requests import get;file =open(f'{scriptPath}','w');file.write( get('https://satyamkumarai.github.io/downloads/create_makefile.py').text);file.close()\"\n\tpy {scriptPath} {dir} -e $(ext)\n")
  
                #make clean
                mkfile.write(f"clean:\n\t{delcommand} \"./*.exe\"")
  
            print("Created in "+os.path.join(dir,"makefile"))
                

            
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



