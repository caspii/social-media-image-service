# Building container
docker build -t getting-started .

t = "Tag", gives the container a name


# Starting a container
docker run -dp 3000:3000 getting-started

# List running containers
docker ps

# Stop docker container
docker stop <the-container-id>

# Remove container
docker rm <the-container-id>x^