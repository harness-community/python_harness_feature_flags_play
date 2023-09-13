# Harness Feature Flags with Python

This project demonstrates the use of Harness Feature Flags in a Python application. It fetches client data based on source IP and interacts with the Harness Feature Flags API to retrieve specific feature flag variations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Script Directly](#running-the-script-directly)
  - [Using Docker](#using-docker)
- [Environment Variables](#environment-variables)
- [Contact](#contact)
- [License](#license)

## Prerequisites

- Python 3.11 or higher
- Docker (if you intend to run the application inside a container)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gacerioni/python_harness_feature_flags_play.git
cd your-repo-name
```

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Script Directly

Execute the main script:

```bash
python3 main.py
```

### Using Docker

1. Build the Docker image:

```bash
docker build -t harness-feature-flags-python:v0.0.1 .
```

2. Run the Docker container:

```bash
docker run -e FF_API_KEY=your_api_key -e FF_BASE_URL=your_base_url -e FF_EVENTS_URL=your_events_url -e FF_IP_INFO_URL=your_ip_info_url -e FF_CLIENT_ID=your_client_id -e FF_CLIENT_NAME=your_client_name harness-feature-flags-python:v0.0.1
```

Replace the placeholders (`your_api_key`, `your_base_url`, etc.) with your actual values. If you do not provide them, it will use default values configured in the code (since this is meant to be a Demo).

## Environment Variables

You can override the default configuration by setting the following environment variables:

- `FF_API_KEY`: Your Harness Feature Flags API key.
- `FF_BASE_URL`: The base URL for the Harness Feature Flags API.
- `FF_EVENTS_URL`: The events URL for the Harness Feature Flags API.
- `FF_IP_INFO_URL`: The URL to fetch IP information.
- `FF_CLIENT_ID`: The client ID for the Harness Feature Flags.
- `FF_CLIENT_NAME`: The client name for the Harness Feature Flags.

## Contact

For any questions or feedback, please reach out to:

- [Gabriel Cerioni](https://github.com/gacerioni) - gacerioni@gmail.com
- [My LinkedIn](https://www.linkedin.com/in/gabrielcerioni/)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
