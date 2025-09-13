IMAGE_NAME="infra"

echo "Building Docker image: $IMAGE_NAME ..."

docker compose --project-name $IMAGE_NAME --file ".docker/compose-docker.yaml" --env-file "example.env" build