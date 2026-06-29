FROM python:3.11-slim

# Step 2: Install dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Step 3: Clone project from GitHub
RUN git clone https://github.com/rohan28-code/rbac_dashboard.git .

RUN pip install django

# Step 4: Dynamic port from docker run command
ENV PORT=8000
EXPOSE $PORT

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
