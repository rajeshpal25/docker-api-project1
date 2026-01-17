#  API Fetch Project Docker

A simple Python project that fetches data from an API and saves it as a JSON file. The project is fully **Dockerized**, making it easy to run anywhere without installing Python dependencies locally.

---

## Features

- Fetch data from any REST API endpoint
- Save API response to a JSON file
- Dockerized for easy deployment
- Lightweight and easy to extend

---

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your system
- Optional: Python 3.x if you want to run locally without Docker

---

## Project Structure

app_v1/
├── app_v1.py # Main Python script to fetch API data
├── Dockerfile # Docker build instructions
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/docker-api-project.git
cd docker-api-project
```

2. Build the Docker Image
```bash
docker build -t api-project .
```
This will create a Docker image named api-project.

3. Run the Docker Container
```bash
docker run --name api-container api-project
```
By default, the JSON output will be saved inside the container.

4. Persist JSON Output to Local Folder
To save the output to your local machine, mount a volume:

```bash
docker run -v $(pwd)/output:/app_v1 api-project
```
$(pwd)/output → local folder to save data.json

/app_v1 → path inside the container where the script writes the file
The API response will be available as output/data.json.


Running Locally (Optional)
If you want to test without Docker:
pip install -r requirements.txt
python app_v1.py
This will create data.json in your project folder.

---

### Notes
json is part of Python’s standard library; no need to install via pip.

You can easily replace the API URL in app_v1.py to fetch different data.
---

## License

This project is open source licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


