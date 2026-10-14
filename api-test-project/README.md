# Memes API Tests

Integration tests for an external Memes API, built with Python, pytest, and
requests. The suite covers authorization, meme creation, retrieval, updates,
and deletion, as well as missing required fields and retrieval of deleted
records. Allure provides test metadata and report results.

The tests call an external API and create/delete records. Run them only against
a service intended for testing. Created records are registered for cleanup
before test assertions run, so cleanup also runs when a test fails. Cleanup
accepts records that have already been deleted and verifies their absence with
a GET request expecting HTTP 404. Cleanup may fail if the process is forcibly
terminated or the network is unavailable. During a normal run, cleanup failures
are reported as teardown errors.

## Installation

Run the commands from the `api-test-project` directory. Tested with Python 3.14.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\activate`.
The `.venv` environment is excluded from Git and must be created locally.

## Configuration

The default API URL is `http://memesapi.course.qa-practice.com`.
To use another test service, set the environment variable before running tests:

```bash
export MEMES_API_BASE_URL="http://your-test-api.example"
```

Settings are defined in `config.py`. The connection timeout is 5 seconds and
the read timeout is 15 seconds. These values do not limit the total test duration.
The name used to obtain a token is set in the `token` fixture in `conftest.py`.
The token is cached in `.pytest_cache`, which is excluded from Git.
When switching services or users, clear the cache with
`python -m pytest --cache-clear`.

## Running Tests

Collect tests without making HTTP requests:

```bash
python -m pytest --collect-only -q
```

Run all tests:

```bash
python -m pytest -q
```

## Allure Reports

Save report results, clearing any previous results in the output directory:

```bash
python -m pytest --alluredir=allure-results --clean-alluredir
```

Viewing reports requires a separately installed Allure CLI and its Java runtime.
The Python package `allure-pytest` does not install the CLI.

```bash
allure serve allure-results
```

Alternatively, generate and open a report:

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Project Structure

- `config.py` — API URL and request timeouts.
- `endpoints/` — HTTP requests and response checks.
- `conftest.py` — authorization, test data setup, and cleanup.
- `tests/` — test scenarios.
