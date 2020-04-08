# Async rest api

[![CI](https://github.com/ammarnajjar/async-rest-api/workflows/ci/badge.svg)](https://github.com/ammarnajjar/async-rest-api/actions)

## Usage:

- In terminal:

```bash
docker-compose up -d --build
```

- Open the swagger interface in browser: [http://localhost:3100/docs](http://localhost:3100/docs)

## To run the tests:

```bash
docker-compose up -d --build
docker-compose exec web pytest --cov
```
