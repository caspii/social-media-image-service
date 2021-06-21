# Building container
docker build -t getting-started .

t = "Tag", gives the container a name


# Starting a container
docker run -dp 3000:3000 getting-started

## Pass an ENV
Define variable in call:
docker run --env PORT=3000 -dp 3000:3000 screenshot-service

Or use variables that you’ve exported to your local environment:
export PORT=3000
docker run --env PORT -dp 3000:3000 screenshot-service

# List running containers
docker ps

# Stop docker container
docker stop <the-container-id>

# Remove container
docker rm <the-container-id>


