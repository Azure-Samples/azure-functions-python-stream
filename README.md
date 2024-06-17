# Azure Functions Python Stream Sample

The apps in this repo demonstrate the Python HTTP streams feature on Azure Functions.

The function app `http_download` receives and processes streaming data from a client in real time. It demonstrates streaming upload capabilities that can be helpful for scenarios like processing continuous data streams and handling event data from IoT devices.

You must use an HTTP client library to make streaming calls to a function's FastAPI endpoints. The client tool or browser you're using might not natively support streaming or could only return the first chunk of data. You can use 'client_script.py' to send streaming data to an HTTP endpoint

The function app `http_upload` is an HTTP triggered function that streams HTTP response data. You might use this functionality to support scenarios like sending event data through a pipeline for real time visualization or detecting anomalies in large sets of data and providing instant notifications.

To run these samples, use the instructions in [Getting started with HTTP Streams using Azure Functions in Python](https://techcommunity.microsoft.com/t5/azure-compute-blog/azure-functions-support-for-http-streams-in-python-is-now-in/ba-p/4146697). For any questions or feedback, please file an issue in the [Azure Functions Python worker repository](https://github.com/Azure/azure-functions-python-worker/issues).
