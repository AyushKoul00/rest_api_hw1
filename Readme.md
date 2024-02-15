# String Manipulation REST API

## Summary of the String Manipulation REST API
The String Manipulation REST API is designed to provide a variety of string-related operations through a simple, easy-to-use interface. This API enables users to perform tasks such as converting strings to upper or lower case, checking for palindromes, counting words, reversing strings, and concatenating multiple strings. Aimed at developers, educational purposes, and anyone interested in string processing, this API offers a convenient way to manipulate and analyze text data.

### Core Technologies and Packages
* **Bottle**: A lightweight Python web framework used for building the REST API. It provides routing, request handling, and response formatting capabilities, making it ideal for small-scale web applications and services.
* **Python Standard Library**: Utilized for various built-in functionalities such as time management (time module) and debugging (pprint module). The API leverages the Python Standard Library to perform string manipulations and to access current system time.
* **Requests**: Although not part of the API implementation itself, the requests library is recommended for testing the API endpoints. It simplifies the process of sending HTTP requests in Python, making it a valuable tool for API testing.
* **AWS EC2**: I created an EC2 instance in which I installed Docker and pulled my docker container of the REST API. I then ran that container on the instance and accessed it using the instance's Public IP address (on port 80)

### How the REST API Works
The API operates over HTTP, allowing clients to interact with it using standard HTTP methods such as GET. Each endpoint corresponds to a specific string operation, with clients providing input through query parameters. The API processes these inputs and returns the results in plain text or JSON format, depending on the endpoint and the requested response type.

For example, to reverse a string, a client would send a GET request to the /reverse endpoint with a string query parameter. The API would then return the reversed string in the response body.

## Testing
API functionality can be tested using tools such as curl or Postman, or by writing automated tests using Python's pytest framework along with the requests library. This ensures each endpoint behaves as expected across various scenarios.

## Conclusion
This REST API showcases the flexibility and power of Python and Bottle for web service development, providing a range of string manipulation capabilities through a simple and intuitive interface. Its design principles emphasize ease of use, making it accessible to both novice and experienced programmers alike.

## Additional Links
* GitHub Link: `https://github.com/AyushKoul00/rest_api_hw1`
* Documentation `Link: https://github.com/AyushKoul00/rest_api_hw1/wiki`
* Docker Hub Link: `https://hub.docker.com/repository/docker/ayushk0ul/rest_api_hw1/general`
* Circle CI Link: `https://app.circleci.com/pipelines/circleci/SBwsLs7BGnbJxPYsEdW9Bs/R6fP9LEwjuabE2s6w86mMi`

## Extra resources (for Learning/Reference)
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
