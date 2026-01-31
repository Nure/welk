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
hello
