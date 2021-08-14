# pokemon-cards-api

## Development
- Build: `docker-compose build`
- Run: `docker-compose up`
- Run tests: `docker-compose run --no-deps api pytest /app`

## Production
- Build: `docker build . -f docker/api/Dockerfile --no-cache -t api`
- Run: `docker run --env-file <env-file> -d -p 5000:5000 --name pokemon-cards api`

## Required Environment Variables
- API_KEY
- DB_USER
- DB_PASS
- DB_HOST
- DB_PORT
- DB_NAME