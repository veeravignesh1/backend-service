# learn-fastapi

docker-compose.yaml file contains two services 
    - nginx
    - api
nginx forwards the request on port 80 to the service running on proxy-api-network port 8000 to get response from the FastAPI service.
