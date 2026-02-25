# Fully functioning ELK stack and a FastAPI application running in a modular, production-ready directory structure.



## Project File Structure

```text
elk-lab/
├── app/
│   ├── main.py             # Entry point: Initializes FastAPI & Logging
│   ├── api/
│   │   └── v1/
│   │       ├── api.py      # Router aggregator: Merges all endpoints
│   │       └── endpoints/
│   │           └── items.py # Actual API logic & routes
│   └── Dockerfile          # Containerizes the Python application
├── logstash/
│   └── pipeline/
│       └── logstash.conf   # Log processing & Grok parsing logic
├── filebeat/
│   └── filebeat.yml        # Log collection & shipping configuration
└── docker-compose.yml      # Orchestrates all 5 services
└── flood_traffic.py        # Traffic Generator that acts as a "simulated user."
```

## Create an EC2 (t3.large) machine

### SSH to the machine

### Run these commands
    sudo apt sudo apt update && sudo apt upgrade -y 


## Install Docker and docker compose
### Install Docker
    sudo apt install docker.io
    docker --version # docker installed
    sudo usermod -aG docker $USER #add user (ubuntu) to the docker group
    sudo reboot # Reboot the EC2 machine and then SSH again
    docker ps # you should see docker is working

### Install Docker Compose V2
```bash
# 1. Create a directory for Docker plugins
mkdir -p ~/.docker/cli-plugins/

# 2. Download the latest version of Docker Compose (v2.32.4)
curl -SL https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose

# 3. Make the file executable
chmod +x ~/.docker/cli-plugins/docker-compose

# 4. Create a link so 'docker compose' works globally
sudo ln -s ~/.docker/cli-plugins/docker-compose /usr/local/bin/docker-compose
docker compose version #It should now return: Docker Compose version v2.*.*.
```

### Clone this repository to the EC2 machine & configure Filebeat
```bash
    git clone https://github.com/Nure/welk.git 
    cd welk
    # Set the correct memory limit for Elastic
    sudo sysctl -w vm.max_map_count=262144

    # Set Filebeat config ownership
    sudo chown root ./filebeat/filebeat.yml
    sudo chmod 644 ./filebeat/filebeat.yml
```


### AWS Security Group Configuration

<p>Before installing anything, ensure your AWS EC2 Instance has the following Inbound Rules enabled in its Security Group:</p>

```bash
Port	Protocol	Purpose	Source
22	    TCP	        SSH Access	Your IP
5601	TCP	        Kibana Web UI	Your IP (or 0.0.0.0/0 for lab)
9200	TCP	        Elasticsearch API	Internal (or App Server IP)
5044	TCP	        Logstash Beats Input	Filebeat IP (Same server here)
8000    TCP         FastAPI Runs on the Port
```

## Run your FastAPI application and ELK stack with Docker Compose
```bash
# Start everything in the background
docker compose up -d

# If you made changes to your FastAPI code and need to rebuild the image
docker compose up --build -d

docker ps # you should see welk-filebeat-1, welk-kibana-1, welk-logstash-1, welk-elasticsearch-1 and welk-fastapi-app-1 containers are running

```

## Check FastAPI App log and Filebeat log
    docker logs welk-fastapi-app-1
    docker logs welk-filebeat-1 --tail 20

## Generate Traffic from your FastAPI:
### Open your browser and visit 
```bash 
http://<AWS_IP>:8000/api/v1/items/
```

## Create ElasticSearch log view
1. Create a "Data View". At the top left and click the Hamburger Menu (☰)

    Scroll down to the very bottom and click Stack Management.

    On the left sidebar, under the Kibana section, click Data Views

    Click the blue Create data view button.

2. Connect to your FastAPI Logs
    Name: Enter fastapi-logs-*.

    Index pattern: Enter fastapi-logs-*.

    If everything is working, you should see a matching index name appear on the right side.

    Timestamp field: Select @timestamp from the dropdown.

    Click Save data view to Kibana.

3. View the Logs
    Click the Hamburger Menu (☰) again.

    Click Discover (it's usually near the top).

    Ensure your new fastapi-logs-* data view is selected in the dropdown on the left.

    You should now see your Python logs appearing in the table!


## Generating Traffic for ELK

### Check current Python version
    python3 --version

### Install Pip3
    sudo apt install -y python3-pip

    pip3 --version #verify PIP installation

### Install Requests Library (quick installation)
    pip3 install requests --break-system-packages

### Generating Traffic. ELK stack is "silent" until logs are produced. You must generate activity:

<p>Go to your flood_traffic.py file and change API_BASE_URL = "http://localhost:8000/api/v1" to API_BASE_URL = "http://ec2-machine-ip:8000/api/v1"</p>

    python3 flood_traffic.py -rate 50  
    

Most load-testing scripts use this number (-rate 50) to mean "Send 50 requests every second."

    ctr + c # Stop the load script


## Stop the Full Process

Run this command once your testing is done and you do not need to play around this project

    docker compose down

## Terminate (delete) Your EC2 Instance

It is important to de-provision your EC2 machine to avoid additional charge by AWS. No Instance, no charge.

---

CHEERS!