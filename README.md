# nginx-fastapi



docker-compose.yaml file contains two services 
- nginx
- api

![nginx-fastapi architecture](https://github.com/veeravignesh1/learn-fastapi/blob/nginx-fastapi/nginx-fastapi.png)

Nginx forwards the request on port 80 to the service running on proxy-api-network port 8000 to get response from the FastAPI service.
