FROM mcr.microsoft.com/devcontainers/base:noble

# Update layer
RUN apt update

# Clean layer
RUN apt-get clean

# Download and install uv as package manager
# Install python 3.13
RUN \
    wget https://astral.sh/uv/install.sh && \
    sh install.sh && \
    /root/.local/bin/uv python install 3.13

COPY . .