
echo "Starting services with docker-compose ..."

docker compose --file ".docker/compose-docker.yaml" --env-file "example.env" up -d --build