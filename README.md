# angry_api_service

This repo contains Python-based API web-service based on **aiohttp** and **Click**. It is made as per test task.

Test task can be found by following the link below:

https://4kex.notion.site/Middle-Python-90e58234c3be44a8a32e73730df9a242


____________________________________________________________________________________________________________________________________________________
## Table of Contents

- [Installation](#installation)
- [Endpoints description](#endpoints)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Documentation used](#documentation)


____________________________________________________________________________________________________________________________________________________
## Installation

To install and set up the project, follow these steps:

1. Clone the repository:

```$ git clone hhttps://github.com/iduseev/angry_api_service.git```


2. Create & activate python **venv**:

```$ python -m venv .venv```

```$ source .venv/bin/activate```


3. Install the project dependencies within the activated python **venv** based on **pyproject.toml**:

```$ pip install -e .```

Once you’ve run this command, then your **angry_api_service** app will be installed in your current Python environment. You can check it out by running the following command:

```$ pip list```

**angry_api_service** should appear among other currently installed packages in a given environment.

You can ensure that the command ``run_server`` is now available within the activated python venv by checking the *.venv\bin* folder contents where the command ``run_server`` should now become available.

4. Run the web server using terminal:

```$ run_server```

The web-server will run on ``localhost`` using port ``8080`` as default. However, you can override default values for **host** and **port** using additional flags as per example:

```$ run_server --host 127.0.0.1 --port 8000```



The web server can also be run in Docker. Follow these steps to containerize this application.

1. Ensure that you are located within the project directory:

```$ cd /path/to/angry_api_service```


2. Build the web-app's image:

```$ docker build -t angry_api_service .```

3. Start an app container:

```$ docker run -dp 127.0.0.1:8080:8080 angry_api_service```

4. After a few seconds, open your web browser to http://localhost:8080. You should see the greeting message *Hello, world*


____________________________________________________________________________________________________________________________________________________
## Endpoints

1. GET ```/``` - **"hello"** endpoint, returns a greeting message to check API workability.
   
2. GET ```/healthcheck``` - **"healthcheck"** endpoint, returns empty JSON and ``status code 200`` for each request.

3. POST ```/hash``` - **"hash_from_string"** endpoint, checks if **string** field is provided within the request body.

If **string** field is provided - calculates a hash of the given value using algorithm sha256.

Returns JSON ``{"hash_string": <calculated hash>}`` and ``status code 200``.

Otherwise returns JSON ``{"validation errors": <error description>}`` and ``status code 400``.

If encountered an unexpected exception, returns JSON with exception traceback and ``status code 400``.


____________________________________________________________________________________________________________________________________________________
## Contributing

If you'd like to contribute to this project, please fork the repository and create a new branch for your changes. Then, submit a pull request with a detailed description of your changes.


____________________________________________________________________________________________________________________________________________________

## Credits

Kudos to the **aiohttp** and **Click** development teams for creating a powerful and easy-to-use web framework and a tool for native and convenient way to establish a CLI.


____________________________________________________________________________________________________________________________________________________
## License
This project is licensed under the MIT License.


____________________________________________________________________________________________________________________________________________________
## Documentation

### aiohttp
---------------
https://docs.aiohttp.org/en/stable/web_quickstart.html

https://docs.aiohttp.org/en/stable/web_reference.html

https://docs.aiohttp.org/en/stable/client_quickstart.html

https://docs.aiohttp.org/_/downloads/en/v3.7.4/pdf/

https://github.com/aio-libs/aiohttp

https://github.com/aio-libs/aiohttp-demos

https://realpython.com/async-io-python/

https://github.com/aio-libs/aiohttp/issues/1155

https://www.youtube.com/watch?v=Z784Mwm4VBg


### Click
---------------
https://realpython.com/python-click/

https://click.palletsprojects.com/en/latest/entry-points/



### pyproject.toml
---------------
https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

https://packaging.python.org/en/latest/specifications/entry-points/

https://stackoverflow.com/questions/62408719/download-dependencies-declared-in-pyproject-toml-using-pip

https://stackoverflow.com/questions/69711606/how-to-install-a-package-using-pip-in-editable-mode-with-pyproject-toml


### testing
---------------
https://docs.aiohttp.org/en/stable/testing.html

https://stackoverflow.com/questions/70015634/how-to-test-async-function-using-pytest


### Docker
---------------
https://docs.docker.com/get-started/02_our_app/
