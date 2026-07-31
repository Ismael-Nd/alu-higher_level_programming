# python-network_0

This project covers the basics of HTTP using `curl` from Bash
scripts: reading response size and body, filtering by status code,
sending different HTTP methods (DELETE, OPTIONS), setting custom
request headers, and sending POST parameters.

## Tasks

| File | Description |
| --- | --- |
| 0-body_size.sh | Displays the size, in bytes, of a response body |
| 1-body.sh | Displays the response body, only for a 200 status code |
| 2-delete.sh | Sends a DELETE request and displays the response body |
| 3-methods.sh | Displays all HTTP methods accepted by the server |
| 4-header.sh | Sends a GET request with a custom header |
| 5-post_params.sh | Sends a POST request with `email` and `subject` parameters |

## Usage

Each script is tested against the web server running on port 5000 in
the provided container:

```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
./2-delete.sh 0.0.0.0:5000/route_3
./3-methods.sh 0.0.0.0:5000/route_4
./4-header.sh 0.0.0.0:5000/route_5
./5-post_params.sh 0.0.0.0:5000/route_6
```
