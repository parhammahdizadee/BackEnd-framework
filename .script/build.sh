IMAGE_NAME="infra"

echo "Building Docker image: $IMAGE_NAME ..."
docker build -f .docker/Dockerfile -t $IMAGE_NAME ..