
```
npm install vite
npm run build-only
```

```
docker build -t test:latest . 
docker run -it -p8888:80 test:latest
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

### deploy
```
gcloud builds submit . --tag=asia-northeast3-docker.pkg.dev/{Project_id}/{projectname}/{imagename}:1.0.5 

```