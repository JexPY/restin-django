# Restin-Django (+ djangorestframework) with Postgres, Gunicorn, PgAdmin and Nginx



## Introduction
Restin-Django is created to simplify dockerising django projects. If you have any idea feel free to create pull request.

### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml* file.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

    PgAdmin is avaliable at [http://localhost:5555](http://localhost:5555). 
    ```
    email: pgadmin4@pgadmin.org
    pass:  admin
    ```

### Production

Uses gunicorn + nginx.

1. Rename *.env-sample* to *.env* and *.env.db-sample* to *.env.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

## Want to learn how to build this?

- Check out the [post](https://testdriven.io/dockerizing-django-with-postgres-gunicorn-and-nginx).
- Check out also this [post](https://medium.com/@michealjroberts/using-docker-compose-to-setup-a-simple-django-postgresql-application-46cb22521286).
- Check out for pgAdmin [post](https://medium.com/@lvthillo/connect-from-local-machine-to-postgresql-docker-container-f785f00461a7)

## TODO

1. Demo migrations for testing api responces
2. S3 support for static files
3. Redis Cache support
4. CI/CD support (AWS, CE2) 
5. Travis Deployment.


