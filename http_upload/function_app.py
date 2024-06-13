# This example is an HTTP triggered function that streams HTTP response data.
# You might use these capabilities to support scenarios like sending event data 
# through a pipeline for real time visualization or detecting anomalies in 
# large sets of data and providing instant notifications.

import time
import azure.functions as func
from azurefunctions.extensions.http.fastapi import Request, StreamingResponse

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


def generate_count():
    """Generate a stream of chronological numbers."""
    count = 0
    while True:
        yield f"counting, {count}\n\n"
        count += 1

@app.route(route="stream", methods=[func.HttpMethod.GET])
async def stream_count(req: Request) -> StreamingResponse:
    """Endpoint to stream of chronological numbers."""
    return StreamingResponse(generate_count(), media_type="text/event-stream")