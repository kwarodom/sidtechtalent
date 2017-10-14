# docker-ml-django

## Prerequisite
Docker for Mac https://docs.docker.com/docker-for-mac/install/
Docker for Windows 10 https://docs.docker.com/docker-for-windows/install/

## Start docker container
Open terminal or cmd on Windows
```bash
docker-compose up --build
```

## Access exmaple API
Open browser and browse to
```
http://localhost:8000/api/hello
```

## ML implementation
Implement your ML code at
```txt
sidtechtalent/api/views.py
```

Then update path at 
```txt
sidtechtalent/sidtechtalent/urls.py
```
