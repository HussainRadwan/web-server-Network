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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
