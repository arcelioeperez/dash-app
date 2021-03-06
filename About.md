---
title: About
---  

## Files to Download:  
Required files (download from browser): [insurance.csv](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/insurance.csv) | [requirements.txt](https://raw.githubusercontent.com/arcelioeperez/dash-app/main/assets/requirements.txt) | [app.py](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/app.py) | [eapp - Executable](https://github.com/arcelioeperez/dash-app/raw/gh-pages/source/eapp)  

Download here: 
<a target = "_blank" href="source/insurance.csv" download>insurance.csv</a> | <a href="source/requirements.txt" download>requirements.txt</a> | <a target = "_blank" href="source/app.py" download>app.py</a>  

All in one folder - including Makefile: [Files](https://github.com/arcelioeperez/dash-app/tree/gh-pages/source)     
Optional - only the makefile: [Makefile](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/source/makefile)  
             
GitHub:   
[GitHub Repository](https://github.com/arcelioeperez/dash-app/tree/gh-pages) | [GitHub Pages](https://arcelioeperez.github.io/dash-app/)  
## Running on Windows:   
### Running with Make:  
If you don't have Make installed you could install it by downloading it on this [website](http://gnuwin32.sourceforge.net/packages/make.htm).  
You could also download and install 'Chocolatey', which is a package manager for Windows.  
Download Chocolatey: [Chocolatey - Windows Package Manager](https://chocolatey.org/)  

**Use a Unix-like terminal like Git Bash or Powershell - it makes running programs easier**   

> Make sure that you have Python in your **path** otherwise it won't recognize the **python** command.  

```
#installing Make with Chocolatey 
choco install make 
```  

Running the *app.py* file with *make*:  
```
#installing all the packages with one command
make packages
#then running the app.py file
make app
```  

### If you don't want to use Make:  
```
#installing all the packages with requirements.txt
pip install -r requirements.txt
#then running app.py
python app.py
```  

>*After running the above commands - either with or without make - you must go the localhost link i.e. http://127.0.0.1:8050/*   

## Running with Anaconda:  
### Running with Spyder (IDE):  

Click the **run** button and then go to the link that is displayed in the terminal, i.e. **http://127.0.0.1:8050/**  

### Running from the Anaconda Prompt:  

```
#going to the directory (folder)
cd foldername 
#running the app 
python app.py
```  

## Running on MacOS or GNU-Linux  
### Running with Make:  

Open the terminal and check if you have *make* installed  

```
make --version
```  
*If you don't have it installed, you can install it with Homebrew - a package manager for MacOS*  

### Installing *make* with Brew   
Download Brew: [Homebrew - MacOS Package Manager](https://brew.sh/)  
```
brew install make
```   
### Run Without Using Make  
```
python3 app.py
```  
**Note: When installing packages with `pip` you must also type `pip3` in order to run Python 3.**


**Note: all the files must be in the same directory (folder) and all the packages must be installed prior to running `app.py`.**  

### Overview of Unix/GNU-Linux Commands
Once all the files are in one folder:  
```
# Go to the folder by typing 
cd foldername 
```  
Listing all the files inside the folder:  
```
ls
```  
Opening a file with VI or VIM:  
```
vi filename
#or 
vim filename
```  
Renaming file:  
```
mv filename newfilename
```  
Moving a file to another directory (folder):  
```
mv filename nameofthedirectory/
```  
What is your current directory:  
```
pwd
```  
Home Directory:  
```
~/
#for example, going to the *app* directory from the *xyz* directory 
cd ~/app
```  
Going to the previous directory:  
```
cd .. 
```
Removing (deleting) a file:  
```
rm filename
#or force remove
rm -rf filename
```  
Opening a website from the Terminal:  
```
#MacOS 
open https:// ... 
#Linux, where the | means "OR"
xdg-open file | url
```  

### Running a GNU-Linux Terminal on Windows  
There are also ways of installing a Linux Distribuition Terminal on Windows.    
Ubuntu, Debian, openSUSE, and Kali Linux could be installed using the Windows Subsystem for Linux (WSL).    

Enabling WSL - go to Powershell as an administrator and type   
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
After doing this you can download any Linux distribuition available at the Windows Store.  
**Note:** You would have to check if Python is installed as well as other dependencies.  
```
#checks the version of Python 3
python3 -V
```  
Installing Python 3, if you don't have it  
```
sudo apt-get update 
sudo apt-get install python3 #Debian and Ubuntu
#installing pip3
sudo apt-get install python3-pip
```    
**Use 'dnf' instead of apt if using Fedora, or 'yum' if using CentOS. Also, make sure to check which package manager your distribution uses.**  

Installing **make** - this will install **g++**, **gcc**, and **make**  

>gcc is the C compiler   
>g++ is the C++ compiler  

```
sudo apt-get update 
sudo apt-get install build-essential
```  

#### **Note:** if you do not have the required packages you must type this in your command prompt (or Git), Terminal (MacOS) or GNU-Linux Terminal   
```
pip install -r requirements.txt
#or 
make packages
```    
**requirements.txt** contains all the libraries and dependencies needed to run **app.py**  - also, as explained above, the Makefile contains the 'make packages' which runs the `pip install -r requirements.txt` command  

### Running the `eapp` executable  
```
./eapp 
```  
**After this command, you have to go to the URL that appears on the terminal.**
