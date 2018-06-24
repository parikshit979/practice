# URL Shortener

Simple Flask application for Url Shortener.

### Apis
- Get all short urls.
    ```sh
  - GET /url
    ```
 - Generate short url.
    ```sh
    - POST /url {"url": "https://www.gogle.com"}
    ```
 - Delete short url.
    ```sh
        - DELETE /url/{id}
    ```
- Redirect to original website.
    ```sh
    - POST /{short_url}
    ```
- Check if expression is parenthesized.
    ```sh
    - POST /parenthesis {"expression": "((([[]]))"}
    ```

### Installation

Url Shortener requires Python 2.7 to run.

Install the dependencies and start the server.

```sh
$ pip install -r requirements.txt
$ APP_SETTINGS=development python run.py
```

For production environments...

```sh
$ APP_SETTINGS=production python run.py
```

### DB Setup
  - Initialize Database
  ```sh
        $ APP_SETTINGS=development python migrate.py db int
  ```
  - Migrate Database
  ```sh
        $ APP_SETTINGS=development python migrate.py db migrate
  ```
  - Apply Upgrade
  ```sh
        $ APP_SETTINGS=development python migrate.py db upgrade
  ```

### Docker
Url Shortener is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 5000, so change this within the docker-compose.yml if necessary. When ready, simply use the docker-compose.yml to build the image.

```sh
$ cd UrlShortner
$ docker-compose -f docker-compose.yml up --build
```
This will create the **urlshortner** image and start the service. 

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://127.0.0.1:5000/url
```

### Testing

For testing environments...

```sh
$ APP_SETTINGS=testing python test_apis.py
```
