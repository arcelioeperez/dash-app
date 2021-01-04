# Using Docker  

View the Dockerfile: [here](https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/Dockerfile)  

Download with `wget`:  
```
wget https://raw.githubusercontent.com/arcelioeperez/dash-app/gh-pages/Dockerfile
```

**Installing Docker**  

MacOS  
```
brew cask install docker
```  

GNU-Linux (Depending on the package manager)  
```
sudo apt install docker-ce
```  

Windows  
Download from the official Docker website.  

**Build the Docker Image**    
```
sudo docker build /path/to/the/dockerfile -t dash-app
```  

**Run the image**    

```
sudo docker run -p 8080:80 dash-app
```  

Open localhost at http://localhost:8080/. Or any other host that you defined in your app.


**More information: [Docker.com](https://docs.docker.com/get-docker/)**  
