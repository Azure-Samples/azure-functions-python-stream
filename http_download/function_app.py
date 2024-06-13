# This example is an HTTP triggered function that receives and processes streaming data 
# from a client in real time. It demonstrates streaming upload capabilities that can be 
# helpful for scenarios like processing continuous data streams and handling event data 
# from IoT devices.

# You must use an HTTP client library to make streaming calls to a function's FastAPI 
# endpoints. The client tool or browser you're using might not natively support streaming 
# or could only return the first chunk of data. You can use 'client_script.py' to 
# send streaming data to an HTTP endpoint

import azure.functions as func
from azurefunctions.extensions.http.fastapi import JSONResponse, Request

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="streaming_upload", methods=[func.HttpMethod.POST])
async def streaming_upload(req: Request) -> JSONResponse:
    """Handle streaming upload requests."""
    # Process each chunk of data as it arrives
    async for chunk in req.stream():
        process_data_chunk(chunk)

    # Once all data is received, return a JSON response indicating successful processing
    return JSONResponse({"status": "Data uploaded and processed successfully"})


def process_data_chunk(chunk: bytes):
    """Process each data chunk."""
    # Add custom processing logic here
    pass