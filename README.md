# Deploying Machine Learning FastAPI on Google Cloud Run - README.md

This guide will walk you through the process of deploying the Machine Learning FastAPI project on Google Cloud Run. It assumes that you have already built a Docker image for the project and have the necessary credentials and permissions to deploy on Google Cloud.

## Prerequisites

Before deploying the project, make sure you have the following:

- Docker installed on your local machine
- A Google Cloud account with the necessary credentials and permissions
- The project's Docker image built and tagged locally

## Deployment Steps

Follow the steps below to deploy the Machine Learning FastAPI project on Google Cloud Run.

### 1. Build the Docker Image

First, build the Docker image for the project using the provided Dockerfile. Open a terminal or command prompt in the project directory and run the following command:

```shell
docker build -t nlp-fastapi:latest .
```

### 2. Tag the Docker Image

Next, tag the Docker image with the appropriate repository information. Run the following command to tag the image:

```shell
docker tag nlp-fastapi asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi
```

Replace `asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi` with your desired image repository location.

### 3. Push the Docker Image

Push the Docker image to the configured container registry using the following command:

```shell
docker push asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi
```

Replace `asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi` with your image repository location.

### 4. Deploy on Google Cloud Run

Now, deploy the Docker image on Google Cloud Run. Run the following command:

```shell
gcloud run deploy default-service \
    --image asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi \
    --region asia-southeast2 \
    --platform managed \
    --allow-unauthenticated \
    --port 80 \
    --memory 4Gi
```

Make sure to replace `asia-southeast2-docker.pkg.dev/serfee-project/nlp-images/nlp-fastapi` with your image repository location and configure the deployment options (region, platform, authentication, port, memory) as per your requirements.

### 5. Access the Deployed Application

After the deployment is successful, you can access the deployed application using the provided URL. You should see the API documentation and be able to make requests to the API.

## Additional Notes

- Ensure that you have the necessary permissions and credentials to deploy on Google Cloud Run.
- Modify the deployment command and options as per your specific requirements.
- You may need to authenticate and configure your gcloud CLI with your Google Cloud account before deploying.

## Contributing

Contributions are welcome! If you find any issues or want to add new features to this deployment guide, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).