import os
import glob

# This function will open and append content to depoy file
def open_write_content(file):
    with open(file) as curr_file:
        lines=curr_file.readlines()
        lines.append("\n\n") # appears after each file
        with open(parent_location+"\\"+patch_name+"\\"+deploy_script_file_name , "a") as write_file:
            write_file.writelines(lines)
        

#finds out all files in specified folder and invokes write file function
def append_all_files (folder ,extn):
    os.chdir(folder)
    #print(f"Current working directory : {os.getcwd()} ")
    files_arr= [f for f in glob.glob("*."+extn)]
    files_arr.sort()
    #For esch file found , get the ontent in ppaend mode
    for i in files_arr:
        open_write_content(i)



patch_name ="Jul2022"
deploy_script_file_name = "deploy_script.sql"
parent_location = os.getcwd()
#patch_folder_type =["ddl" ,"dml" ,"views","triggers" , "packages"]
patch_folder_type =["ddl" , "dml" ,"final" ] # for testing
print(f"Current working directory : {os.getcwd()} ")



for i in patch_folder_type:
    os.chdir(parent_location)
    append_all_files(f"{patch_name}\{i}" , "sql")

