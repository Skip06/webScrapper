Architecture

    Fetcher: Asynchronous HTTP/2 networking using HTTPX for connection pooling.

    Parser: Low-latency HTML extraction using the C-based Selectolax engine.

    Models: Strict data validation and schema enforcement via Pydantic.

  Manager: uv (Rust-based package resolver)

Automation: Makefile (Task orchestration)

Logging: Loguru (Structured system logs)  

### 1. Installation

```bash
git clone https://github.com/Skip06/kernel-scraper.git
cd kernel-scraper
uv sync 
```


### 2. Execution

```bash
make run    # Execute the scraper
make clean  # Purge __pycache__ and local data
