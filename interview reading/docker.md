# Docker Interview Questions

## 🐳 Basic Level Questions

### 1. What is Docker and why is it used?
**Answer:** Docker is a containerization platform that packages applications and their dependencies into lightweight, portable containers. It's used for:
- Application deployment consistency - Same container = same behavior everywhere (dev, test, production)
- Environment isolation - Multiple apps on one server conflict with each other
- Resource efficiency - Faster startup (seconds vs minutes)
- Scalability -Instant horizontal scaling during traffic spikes
- DevOps automation - Automated testing and deployment, Consistent deployments,Easy rollbacks,Infrastructure as code
- Containers can reach each other by service name
- Multi-container apps: Easily manage Django + PostgreSQL + Redis

### 2. What's the difference between Docker Images and Docker Containers?
**Answer:**
- **Docker Image**: Read-only template used to create containers (like a blueprint)
- **Docker Container**: Running instance of an image (like a house built from blueprint)

### 3. What is a Dockerfile?
**Answer:** A text file containing instructions to build a Docker image. It defines:
- Base image
- Dependencies
- Configuration
- Commands to run

- `FROM` - Base image (python:3.11-slim)
- `WORKDIR` - Sets working directory inside container /app
- `COPY` - Copies files from host to container ie requirements file
- `RUN` - Executes commands during build ie install sys requirements
- `USER` - Switches to non-root user for security
- `EXPOSE` - Documents which port the app uses
- `ENV` - Sets environment variables
- `CMD` - Default command when container starts

### 4. Explain the basic Docker commands
**Answer:**
```bash
docker build -t myapp .          # Build image and Tags the image with the name "myapp"
- Docker reads the Dockerfile in your current directory
- Executes each instruction (FROM, RUN, COPY, etc.) in order
- Creates layers for each instruction to enable caching
- Tags the final image as "myapp"
- Stores the image locally on your machine
docker run -d -p 8080:80 myapp   # Run container in detached mode in the background
docker ps                        # List running containers
docker images                    # List images
docker stop <container_id>       # Stop container
docker rm <container_id>         # Remove container
docker rmi <image_id>           # Remove image
```

##### docker-compose
- Builds your image (same as docker build -t myapp .)
- Starts all services with proper port mapping
- Creates a network so containers can talk to each other
- Manages dependencies (web service waits for database)
- Sets environment variables
- Mounts volumes for data persistence

```bash
docker-compose up -d        # Start all services in background
docker-compose down         # Stop and remove all containers
docker-compose logs web     # View logs for specific service
docker-compose exec web bash # Execute commands in running container
```

### 5. What are Docker layers?
**Answer:** Docker images are built in layers. Each instruction in Dockerfile creates a new layer. Layers are:
- Read-only
- Cached for efficiency
- Shared between images
- Stacked on top of each other

## 🚀 Intermediate Level Questions

### 6. What is Docker Compose?
**Answer:** Tool for defining and running multi-container Docker applications using YAML files.


### 7. Explain Docker networking modes
**Answer:**
- **Bridge**: Default network for containers
- **Host**: Container uses host's network stack
- **None**: No network access
- **Overlay**: Multi-host networking for Swarm
- **Custom**: User-defined networks

### 8. What are Docker volumes?
**Answer:** Persistent data storage mechanism that exists outside container lifecycle.

**Types:**
```
# Named volume
docker run -d -v myvolume:/data nginx

# Bind mount  
docker run -d -v /host/path:/container/path nginx

# Anonymous volume
docker run -d -v /data nginx
```


### 9. What's the difference between COPY and ADD in Dockerfile?
**Answer:**
- **COPY**: Simply copies files/directories
- **ADD**: Copies + can extract tar files and download URLs
- **Best Practice**: Use COPY unless you need ADD's extra features

### 10. How do you optimize Docker images?
**Answer:**
- Use smaller base images (alpine) -> a lightweight Linux distribution commonly used as a base for Docker images.
- Multi-stage builds
- Minimize layers
- Remove unnecessary packages
- Use .dockerignore
- Cache dependencies separately



## 🏗️ Advanced Level Questions

### 11. What is Docker Swarm?
**Answer:** Docker's native clustering and orchestration(automated coordination and management of multiple containers, services, or systems working together.) tool for managing multiple Docker hosts.

**Key concepts:**
- **Nodes**: Manager and worker nodes
- **Services**: Desired state of application
- **Tasks**: Individual containers
- **Stack**: Group of related services

### 12. How does Docker security work?
**Answer:**
- **Namespaces**: Process isolation
- **Cgroups**: Resource limiting
- **Capabilities**: Privilege restrictions
- **Seccomp**: System call filtering
- **AppArmor/SELinux**: Mandatory access control

**Security best practices:**
```bash
# Run as non-root user
USER 1001

# Read-only filesystem
docker run --read-only myapp

# Drop capabilities
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE myapp
```

### 13. Explain Docker storage drivers
**Answer:**
- **overlay2**: Default, best performance
- **aufs**: Legacy, still used
- **devicemapper**: Block-level storage
- **btrfs**: Copy-on-write filesystem
- **zfs**: Advanced filesystem features

### 14. What are Docker secrets in Swarm?
**Answer:** Secure way to manage sensitive data in Swarm mode.

```bash
# Create secret
echo "mysecretpassword" | docker secret create db_password -

# Use in service
docker service create \
  --secret db_password \
  --env DB_PASSWORD_FILE=/run/secrets/db_password \
  myapp
```

### 15. How do you troubleshoot Docker containers?
**Answer:**
```bash
# Check logs
docker logs <container_id>

# Execute commands in running container
docker exec -it <container_id> /bin/bash

# Inspect container details
docker inspect <container_id>

# Monitor resource usage
docker stats

# Check container processes
docker top <container_id>
```

## 🔧 Practical/Scenario Questions

### 16. How would you implement a CI/CD pipeline with Docker?
**GitHub Actions + Docker CI/CD:**

When you push code to the main branch, GitHub Actions automatically triggers a workflow that handles your entire deployment process. The workflow first builds a Docker image from your code and runs tests inside a container to ensure everything works correctly. If the tests pass, it logs into Docker Hub and pushes the newly built image to your registry for storage.

After the image is successfully pushed, the workflow connects to your production server via SSH and pulls the latest image from Docker Hub. It then stops the old container, removes it, and starts a new container with the updated code, making your changes live on the server. This entire process happens automatically without any manual intervention, ensuring your application is always tested before deployment and maintaining consistent environments from development to production.

#### Key benefits:
- Consistent environments everywhere
- Fast deployments (just pull new image)
- Automated testing prevents bad code going live
- Easy rollbacks to previous versions

**Answer:**
```yaml
# GitLab CI example
stages:
  - build
  - test
  - deploy

build:
  stage: build
  script:
    - docker build -t myapp:$CI_COMMIT_SHA .
    - docker push myapp:$CI_COMMIT_SHA

test:
  stage: test
  script:
    - docker run --rm myapp:$CI_COMMIT_SHA npm test

deploy:
  stage: deploy
  script:
    - docker service update --image myapp:$CI_COMMIT_SHA myservice
```


### 17. How do you handle database persistence in Docker?
- Using volumes

### 18. How would you scale a Docker application?
**Answer:**
- **Horizontal scaling**: Multiple container instances
- **Load balancing**: Distribute traffic
- **Auto-scaling**: Based on metrics

```bash
# Docker Swarm scaling
docker service scale myapp=5

# Docker Compose scaling
docker-compose up --scale web=3
```

### 19. What's your strategy for handling secrets in Docker?
**Answer:**
- Use Docker secrets in Swarm mode
- External secret management (HashiCorp Vault)
- Environment variables for non-sensitive config
- Init containers for secret injection
- Avoid embedding secrets in images

### 20. How do you monitor Docker containers in production?
**Answer:**
- **Logging**: Centralized logging (ELK stack)
- **Metrics**: Prometheus + Grafana
- **Health checks**: Docker health checks
- **APM**: Application performance monitoring

```dockerfile
# Health check example
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```

## 🎯 Performance & Optimization Questions

### 21. How do you optimize Docker build times?
**Answer:**
- Use build cache effectively
- Multi-stage builds -> Multi-stage builds let you use a large build environment to compile your app, then copy only the final result to a small production image, dramatically reducing size from 500MB to 50MB while maintaining full functionality.
- Parallel builds
- .dockerignore optimization (exclude unnecessary files and directories from being sent to the Docker build context)
- Layer ordering optimization

```bash
.git
.gitignore
__pycache__/
.env
*.env
node_modules/
*.lock
venv/
env/
.DS_Store
```
### 22. What are the resource limits you can set on containers?
**Answer:**
```bash
# Memory limit
docker run -m 512m myapp

# CPU limit
docker run --cpus="1.5" myapp

# Swap limit
docker run --memory=1g --memory-swap=2g myapp

# Block IO
docker run --device-read-bps /dev/sda:1mb myapp
```

### 23. How do you debug container networking issues?
**Answer:**
```bash
# Check network configuration
docker network ls
docker network inspect bridge

# Test connectivity
docker exec -it container1 ping container2

# Check port bindings
docker port <container_id>

# Network troubleshooting tools
docker run --rm -it nicolaka/netshoot
```

## 🧠 Architecture & Design Questions

### 24. When would you use Docker vs Virtual Machines?
**Answer:**
**Use Docker when:**
- Microservices architecture
- Rapid deployment needed
- Resource efficiency required
- Consistent environments

**Use VMs when:**
- Different operating systems needed
- Strong isolation required
- Legacy applications
- Different kernel requirements

### 25. How do you design a microservices architecture with Docker?
**Answer:**
- One service per container
- API Gateway pattern
- Service discovery
- Circuit breakers
- Distributed logging/tracing
- Configuration management

```yaml
# Example microservices stack
version: '3.8'
services:
  api-gateway:
    image: nginx:alpine
  user-service:
    image: userservice:latest
  order-service:
    image: orderservice:latest
  database:
    image: postgres:13
```

# Extended Docker Commands (Question 4)

## 🐳 Essential Docker Commands

### **Image Management Commands**
```bash
# Build image from Dockerfile
docker build -t myapp:v1.0 .
docker build -t myapp:latest --no-cache .  # Build without cache

# List all images
docker images
docker image ls

# Remove images
docker rmi <image_id>
docker rmi myapp:v1.0
docker image rm <image_id>

# Remove all unused images
docker image prune
docker image prune -a  # Remove all unused images (not just dangling)

# Pull image from registry
docker pull nginx:alpine
docker pull ubuntu:20.04

# Push image to registry
docker push myregistry/myapp:v1.0

# Tag image
docker tag myapp:latest myregistry/myapp:v1.0

# Image history and details
docker history <image_id>
docker inspect <image_id>

# Save/Load images
docker save -o myapp.tar myapp:latest
docker load -i myapp.tar

# Export/Import containers as images
docker export <container_id> > container.tar
docker import container.tar myapp:imported
```

### **Container Lifecycle Commands**
```bash
# Run containers
docker run -d -p 8080:80 --name webapp nginx        # Detached mode
docker run -it ubuntu:20.04 /bin/bash              # Interactive mode
docker run --rm alpine echo "Hello World"          # Remove after exit
docker run -v /host/path:/container/path nginx      # Volume mount
docker run -e ENV_VAR=value myapp                   # Environment variable
docker run --network mynetwork nginx               # Custom network

# Start/Stop/Restart containers
docker start <container_id>
docker stop <container_id>
docker restart <container_id>
docker pause <container_id>
docker unpause <container_id>

# Kill containers
docker kill <container_id>
docker kill $(docker ps -q)  # Kill all running containers

# Remove containers
docker rm <container_id>
docker rm -f <container_id>   # Force remove running container
docker rm $(docker ps -aq)   # Remove all stopped containers
docker container prune       # Remove all stopped containers
```

### **Container Information & Monitoring**
```bash
# List containers
docker ps                    # Running containers only
docker ps -a                # All containers (running + stopped)
docker ps -q                # Only container IDs
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# Container details
docker inspect <container_id>
docker inspect --format='{{.NetworkSettings.IPAddress}}' <container_id>

# Container logs
docker logs <container_id>
docker logs -f <container_id>        # Follow logs
docker logs --tail 50 <container_id> # Last 50 lines
docker logs --since="2023-01-01" <container_id>

# Container resource usage
docker stats                         # All containers
docker stats <container_id>         # Specific container
docker top <container_id>           # Running processes

# Execute commands in running containers
docker exec -it <container_id> /bin/bash
docker exec <container_id> ls -la
docker exec -u root <container_id> /bin/bash  # As root user

# Copy files to/from containers
docker cp file.txt <container_id>:/path/to/destination
docker cp <container_id>:/path/to/file.txt ./local/path

# Container port information
docker port <container_id>
```

### **Volume Management Commands**
```bash
# Volume operations
docker volume create myvolume
docker volume ls
docker volume inspect myvolume
docker volume rm myvolume
docker volume prune              # Remove unused volumes

# Run with volumes
docker run -v myvolume:/data nginx
docker run -v /host/path:/container/path nginx  # Bind mount
docker run --mount type=volume,source=myvolume,target=/data nginx
```

### **Network Management Commands**
```bash
# Network operations
docker network create mynetwork
docker network create --driver bridge mybridge
docker network ls
docker network inspect mynetwork
docker network rm mynetwork
docker network prune

# Connect/Disconnect containers to networks
docker network connect mynetwork <container_id>
docker network disconnect mynetwork <container_id>

# Run container with custom network
docker run --network mynetwork nginx
```

### **Registry & Repository Commands**
```bash
# Login/Logout from registry
docker login
docker login myregistry.com
docker logout

# Search for images
docker search nginx
docker search --limit 10 ubuntu

# Pull specific versions
docker pull nginx:1.21-alpine
docker pull --all-tags nginx
```

### **System Management Commands**
```bash
# System information
docker version
docker info
docker system df          # Disk usage
docker system events      # Real-time events

# System cleanup
docker system prune       # Remove unused data
docker system prune -a    # Remove all unused data
docker system prune --volumes  # Include volumes

# Remove everything (DANGEROUS!)
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
docker volume rm $(docker volume ls -q)
docker network rm $(docker network ls -q)
```

### **Docker Compose Commands**
```bash
# Compose operations
docker-compose up                    # Start services
docker-compose up -d                # Start in detached mode
docker-compose up --build           # Rebuild images before starting
docker-compose down                 # Stop and remove containers
docker-compose down -v              # Also remove volumes
docker-compose restart              # Restart services
docker-compose pause                # Pause services
docker-compose unpause              # Unpause services

# Service management
docker-compose start <service>
docker-compose stop <service>
docker-compose restart <service>
docker-compose logs <service>
docker-compose logs -f <service>    # Follow logs
docker-compose exec <service> /bin/bash
docker-compose run <service> command

# Scaling
docker-compose up --scale web=3
docker-compose scale web=3

# Configuration
docker-compose config              # Validate compose file
docker-compose ps                  # List compose containers
docker-compose top                 # Display running processes
```

### **Advanced & Debugging Commands**
```bash
# Container filesystem changes
docker diff <container_id>

# Create image from container
docker commit <container_id> myapp:v2.0
docker commit -m "Added feature" <container_id> myapp:v2.0

# Wait for container to exit
docker wait <container_id>

# Get container exit code
docker inspect <container_id> --format='{{.State.ExitCode}}'

# Stream container resource usage statistics
docker stats --no-stream

# Update container configuration
docker update --memory="1g" --cpus="2" <container_id>

# Rename container
docker rename old_name new_name

# Attach to running container
docker attach <container_id>

# Create container without starting
docker create --name mycontainer nginx
```

### **Security & Resource Management Commands**
```bash
# Run with security options
docker run --user 1001:1001 nginx                    # Non-root user
docker run --read-only nginx                         # Read-only filesystem
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE nginx  # Capabilities
docker run --security-opt no-new-privileges nginx    # No privilege escalation

# Resource limits
docker run -m 512m nginx                            # Memory limit
docker run --cpus="1.5" nginx                       # CPU limit
docker run --memory-swap="1g" nginx                 # Swap limit
docker run --pids-limit=100 nginx                   # Process limit
```

### **Multi-Architecture & BuildKit Commands**
```bash
# Multi-platform builds (BuildKit)
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .
docker buildx imagetools inspect myregistry/myapp:latest

# Build with BuildKit features
DOCKER_BUILDKIT=1 docker build --target production .
docker build --build-arg VERSION=1.0 .
docker build --secret id=mysecret,src=./secret.txt .
```

### **Useful Command Combinations**
```bash
# Stop and remove all containers
docker stop $(docker ps -aq) && docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Get IP addresses of all running containers
docker inspect $(docker ps -q) --format='{{.Name}} - {{.NetworkSettings.IPAddress}}'

# Follow logs of multiple containers
docker-compose logs -f web database

# Remove all containers with specific label
docker rm $(docker ps -a --filter "label=app=myapp" -q)

# Backup all volumes
docker run --rm -v $(pwd):/backup -v myvolume:/data alpine tar czf /backup/volume-backup.tar.gz /data
```

These commands cover the complete Docker CLI ecosystem from basic operations to advanced management tasks. Practice these commands to become proficient in Docker operations!