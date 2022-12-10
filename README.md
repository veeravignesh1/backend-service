# nginx-fastapi



docker-compose.yaml file contains two services 
- nginx
- api

![nginx-fastapi](https://user-images.githubusercontent.com/25390522/206836030-6b074ea0-9fcd-44c3-b363-88054edf2532.png)


Nginx forwards the request on port 80 to the service running on proxy-api-network port 8000 to get response from the FastAPI service.
