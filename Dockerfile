FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Step 2: Install python3, pip, and git
RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Step 3: Clone project from GitHub
RUN git clone https://github.com/<your-username>/rbac_dashboard.git .

RUN pip3 install django

# Step 4: Dynamic port from docker run command
ENV PORT=8000
EXPOSE $PORT

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
