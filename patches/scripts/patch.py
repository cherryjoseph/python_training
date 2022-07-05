import os
import glob

# This function will open and append content to depoy file
def open_write_content(file):
    with open(file) as curr_file:
        lines=curr_file.readlines()
        lines.append("\n") # appears after each file
        with open(parent_location+"\deploy_script.sql" , "a") as write_file:
            write_file.writelines(lines)
        

#finds out all files in specified folder and invokes write file function
def append_all_files (folder ,extn):
    os.chdir(folder)
    print(f"Current working directory : {os.getcwd()} ")
    files_arr= [f for f in glob.glob("*."+extn)]
    files_arr.sort()
    #print(files_arr)
    for i in files_arr:
        open_write_content(i)




patch_name ="Jul2022"
#patch_folder_type =["ddl" ,"dml" ,"views","triggers" , "packages"]
patch_folder_type =["ddl" , "dml" ,"final" ] # for testing
parent_location = os.getcwd()
#print(f"Current working directory : {os.getcwd()} ")
#print("  ")
for i in patch_folder_type:
    os.chdir(parent_location)
    append_all_files(f"{patch_name}\{i}" , "sql")

