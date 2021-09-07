## Text File Reader API

[![Docker](https://github.com/PRABIRSOFT/textfilereader/actions/workflows/docker-publish.yml/badge.svg?branch=main)](https://github.com/PRABIRSOFT/textfilereader/actions/workflows/docker-publish.yml)

This application can read content of given file as a http path parameter 
and render properly it in HTML page. Any markup in that file is also preserved.
Enduser can also read the file using line number given in a query param ex: start, end param

## Requirements
Python 3.7.3+

## Usage
To run the server, please execute the following from the root directory:

```
pip install -r requirements.txt
python -m app
```

and open your browser to here:

```
http://localhost:5000/get_file
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t textfilereader:latest .

# starting up a container
docker run -p 5000:5000 textfilereader:latest
```
