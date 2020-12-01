## Errors While Running Scripts  

### Python or Python3  
If you are running on Windows you might have to adjust some files. If you would like to install all the dependencies or run programs then you have to use:  
```
python nameofthefile.py
#and for pip
pip install -r requirements.txt
```  

For Linux, MacOS, or any other Unix-like operating system, the `python3` command is commonly used to differentiate it from the `python` command which is associated with Python 2.  

### Where is Python installed?  
If you are running Windows, try installing either a WSL (Windows Subsytem for Linux) terminal, Powershell terminal or Git Bash terminal. The reason is that you will be able to use Linux commands and follow along the steps.  

If you are running MacOS or Linux (or Windows with any of the aforementioned terminals), type: 
```
which python3
```
This should return the `path` of the `python3` command. Example: `/usr/bin/python3` - this is the path where the `python3` executable is stored.  

### Using `chmod` and Bash Scripts  
If you want to run the `eapp` file or you want to create a new **bash** script, you must include a `shebang` indicating the location of the Python interpreter.  

Example: 
```
#!/usr/bin/env python3 
```
Making an executable:  
```
chmod +x nameofthefile
```
**Note:** The first line of nameofthefile must be the `shebang` or location of the interpreter.  

Doing this will create an executable, meaning that you will be able to run the file by typing:  
```
./nameofthefile
#or
bash nameofthefile
```
### Error: Wrong Interpreter Python3^M - This Error Usually Happens on Unix-like systems (MacOS and Linux)
**Solution:** this file was generated in a Windows machine running a WSL (Debian). One way to fix this error is to use the `dos2unix` package.  

Downloading on MacOS  
```
brew install dos2unix
```
Downloading on Linux (Debian, Ubuntu, or Linux Mint)  

>*Check your distribution package manager i.e in Fedora you would use `dnf` instead of `apt`*  

```
sudo apt-get install dos2unix
```  

Using dos2unix
```
dos2unix nameofthefile.py
```

