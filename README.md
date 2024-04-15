# Simple web server

The project involves creating a simple web server in Python that listens on port 12345 and serves different responses based on the incoming URL requests
The server parses HTTP requests, serves HTML content, including "main_en.html" with specific content and styling, handles images, links, and group information display, and sends appropriate HTTP headers. Error handling and testing are crucial aspects, ensuring the server functions as intended, providing an interactive web experience when users access URLs like "http://localhost:12345/ar" or "http://localhost:12345/en." The implementation specifics will vary by language, but the core components include socket programming, HTTP request processing, HTML/CSS generation, and serving files to meet the specified conditions.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

##### -Make sure python is installed

Open a command line tool such as Windows Terminal (the default on Windows 11) or Command Prompt (the default on Windows 10). In the command line, type:
```
python
```
If Python is installed, you should see a message like "Python 3"

If it is not Download the latest source release from: 
```
https://www.python.org/downloads/
```
##### -Make sure "socket" module is installed in python
run this code 
```
try:
	import socket
	print("Already installed")
except ImportError as e:
	print("Error -> ", e)
```
if the socket is not installed, it can be installed by launching the Command Prompt in Windows as well as executing the following command:
```
pip install socket
```

### Installing & Running

First create a new File then install all my files in the new file 

Now run "main.py" then Open your preferred web browser and type `http://localhost:12345/` or `http://127.0.0.1:12345/` as following:

https://github.com/HussainRadwan/Network-Creating-a-Server-/assets/161932786/60b067ee-7603-48df-81d8-3afeb0ea859e


## It can do multiple things 
![Screenshot 2023-09-01 112647](https://github.com/HussainRadwan/Network-Creating-a-Server-/assets/161932786/fea4e894-21b6-4329-aa13-c677e22eee3e)

### Opinging other sits 

### Tow interfaces one in English and the other in Arabic 
![image](https://github.com/HussainRadwan/Network-Creating-a-Server-/assets/161932786/bfa6ba33-0a5c-4caf-9a81-f32419e5acde)

### other things like ERROR page and sorting files ..etc
![Screenshot 2023-09-01 115520](https://github.com/HussainRadwan/Network-Creating-a-Server-/assets/161932786/671bd07c-e6be-47d9-94a0-6a8729e9278c)
