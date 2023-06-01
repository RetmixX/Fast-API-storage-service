# Fast-API-storage-service
# Guide installation

``git https://github.com/RetmixX/Fast-API-storage-service.git``

``cd .deploy && cp .env.example .env``

Fill data created .env

``docker compose up -d``

# Address for send request -> localhost:8008/

# Available endpoinds

- @app.get("/")
- @app.post("/file")
- @app.get("/my-collections")
- @app.post("/generate-image")
- @app.get("/download/{file_name}")
