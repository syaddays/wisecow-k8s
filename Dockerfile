# Dockerfile for wisecow
FROM ubuntu:24.04

# noninteractive to avoid tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages: bash (default), netcat (if the script uses it), fortune, cowsay
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    bash \
    curl \
    fortune-mod \
    cowsay \
    inetutils-ping \
    netcat \
 && rm -rf /var/lib/apt/lists/*

# Create app dir
WORKDIR /app

# Copy the wisecow script and make executable
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

# Expose the port the README mentions (4499)
EXPOSE 4499

# Use the script as entrypoint
ENTRYPOINT ["/app/wisecow.sh"]
# If script expects flags or should run bash, adjust accordingly.
