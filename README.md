# spojUploader
for problem-setter and contest-setter

**Author: tconqueror - vice-president of ISP club**

**1. Import:**
To use this script, you need to install some python lib:
- requests
- mammoth

**2. How to use:**
I'm using python27 so it's best support for someone who use python27 like me LOL!!!
- Setup folder:
		![1](https://user-images.githubusercontent.com/52455578/71508597-e89f3f00-28ba-11ea-8d88-7625ea48c7ce.png)
		![2](https://user-images.githubusercontent.com/52455578/71508639-12586600-28bb-11ea-8cf8-8974a6903081.png)
- Run:
		$ python spojUploader.py username password parentname
# Note
1. The script will auto convert any *\*.ans* file to *\*.out* file, remove any *"test"* in the name of the test case (Better for change between pc2 and spoj).
2. You need to confirm the username and the password before run this script.
3. The script will auto find any *\*.docx* in your folder and make it the problem body. If you have any tables in your docx file, please check the problem body after the script finish. I suggest you to choose Arial font for your docx file. And you can use image inside the docx file
4.  It will only upload prolem with ['A'-'Z'] name.

# Example
$ python spojUploader.py username password SPOJUPLOADER 

and your folder have A, B, D, Z child-folder. You will get 4 problems with the code 
- **SPOJUPLOADERA** 
- **SPOJUPLOADERB** 
- **SPOJUPLOADERD**
- **SPOJUPLOADERZ**
