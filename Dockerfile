FROM ubuntu:22.04

# 1. Install Python and Pip (Missing in original)
# We combine these to reduce image layers and clean up the cache to save space
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 2. Copy requirements and install
COPY requirements.txt .

# Use pip3 since Ubuntu 22.04 defaults to that name
RUN pip3 install --no-cache-dir -r requirements.txt

# 3. Copy application code
COPY . .

# 4. Security: Run as non-privileged user
RUN useradd -m myuser
USER myuser

# 5. Run the app
# Use python3 to ensure it hits the correct interpreter
CMD ["python3", "app.py"]
