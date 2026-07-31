# python-network_1

This project covers making HTTP requests from Python, first with the
standard library (`urllib`), then with the third-party `requests`
package: fetching a URL, reading response headers, sending POST data,
handling HTTP errors, and consuming a JSON API with GitHub Basic
Authentication.

## Tasks

| File | Description |
| --- | --- |
| 0-hbtn_status.py | Fetches a URL and prints its body (`urllib`) |
| 1-hbtn_header.py | Prints the `X-Request-Id` response header (`urllib`) |
| 2-post_email.py | Sends a POST request with an `email` parameter (`urllib`) |
| 3-error_code.py | Prints the body, or `Error code: <code>` on HTTP error (`urllib`) |
| 4-hbtn_status.py | Fetches a URL and prints its body (`requests`) |
| 5-hbtn_header.py | Prints the `X-Request-Id` response header (`requests`) |
| 6-post_email.py | Sends a POST request with an `email` parameter (`requests`) |
| 7-error_code.py | Prints the body, or `Error code: <code>` for status >= 400 |
| 8-json_api.py | POSTs a search query and prints `[<id>] <name>` from the JSON result |
| 10-my_github.py | Prints a GitHub user's id via Basic Authentication |

## Usage

Tasks 2, 3, 6, 7 and 8 are meant to be tested against the web server
running on port 5000 in the provided container:

```
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./3-error_code.py http://0.0.0.0:5000/status_401
```
