import os
import requests
import mammoth
import sys

if len(sys.argv) != 4:
    print("You need to insert:")
    print("argv[0] = username")
    print("argv[1] = password")
    print("argv[2] = parentnameofproblem")
    sys.exit()
usn = sys.argv[1]
pwd = sys.argv[2]
pname = sys.argv[3].upper()
payload = {'login_user':usn,'password':pwd}
sess = requests.session()
r = sess.post("https://www.spoj.com/login",data=payload)
def uptest(name, path):
    print("*********************************************************")
    #login
    
    #up test
    url = "https://www.spoj.com/problems/" + pname + name + "/edit/" 
    files = os.listdir(path)
    #find problem body
    a = False
    document = ""
    print("Finding problem body (.docx) file...")
    for file in files:
        if len(file.split('.')) > 1 and file.split('.')[1]=="docx":
            print(file + " found")	
            f = open(path + "/" + file,"rb")
            document = mammoth.convert_to_html(f).value.encode("utf-8")
            f.close()
            a = True
    if a == False:
        print("Cant find any *.docx file. The problem body will take the default value")
        document = "Insert problem body"

    #check wrong format problem test
    #print("\nFinding wrong format problem test\n")
    #for file in files:
    #    p = path + "/test/" + file
    #    newp = p
    #    newp = newp.replace("test",'')
    #    newp = newp.replace("ans","out")
    #    if (newp != p):
    #        os.rename(p, newp)
    #        print(p + "renamed to:" + newp)

    #add problem 
    addurl = "https://www.spoj.com/problems/add/complete/"
    add_payload ={
        "form_action" : "modify_problem",
        "pcode" : pname+ name,
        "name" : pname + name,
        "grow" : "0",
        "sourcelimit" : "5000",
        "resource" : "",
        "interactive" : "0",
        "type" : "0",
        "problemtype" : "0",
        "testable" : "on",
        "comsatuts" : "on",
        "body" : document,
        "42" :"on",
        "111" : "on",
        "1" : "on",
        "44" : "on",
        "new_lang" : "on",
        "Modify" : "Create"
    }
    sess.post(url = addurl,data = add_payload)  
    print("Problem Added")    
    #add test case
    size = count(path)
    print("Dang up test bai: " + name)
    for i in range(size):
        nameIn = path + "/test/" + str(i + 1) + ".in"
        nameOut = path + "/test/" + str(i + 1) + ".out"
        fin = open(nameIn,'rb')
        fout = open(nameOut, 'rb')
        data = {
            "form_action" : "modify_new_testcase",
            "upload" : "upload",
            "testcase" : str(i + 1),
            "in_act" : "w",
            "out_act" : "w",
            "timelimit" : "1",
            "judge" : "1",
            "judge_c" : "0",
            "judge_file" : "", 
            "dos2unix" : "on", 
            "Upload" : "Upload"
        }
        files = {"in_file" : fin, "out_file" : fout}
        r = sess.post(url, data = data, files = files)
        print("Uploading test case " + str(i + 1))
        
###################################################################
def count(path) :
    res = 0
    files = os.listdir(path + "/test") 
    for file in files:
        if len(file.split('.')) == 2 and file.split('.')[1] == "in":
            res = res + 1
    return res
####################################################################
root =  os.getcwd()
folders = os.listdir(root)
for folder in folders:
    if len(folder) == 1 and folder >= "A" and folder <= "Z":
        paths = root + "/" + folder
        files = os.listdir(paths)
        #for file in files: 
            #if file.lower() == "test":
                #path = paths + "\\" + file
        
        name = folder
        uptest(name, paths)
        print("https://www.spoj.com/problems/" + pname + name + " completed")
print("Done")
