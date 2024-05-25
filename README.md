[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat&logo=Redis)](https://redis.io/)
[![Celery](https://img.shields.io/badge/-Celery-464646?style=flat&logo=Celery)](https://docs.celeryq.dev/en/stable/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/-Nginx-464646?style=flat&logo=Nginx)](https://www.nginx.com/)
[![Psycopg2-binary](https://img.shields.io/badge/-Psycopg2--binary-464646?style=flat)](https://pypi.org/project/psycopg2-binary/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat&logo=Gunicorn)](https://gunicorn.org/)
[![Stripe](https://img.shields.io/badge/-Stripe-464646?style=flat&logo=stripe)](https://stripe.com/)


# DJANGO-STORE-SERVER

## Table of Contents

- [Project Description](#project-description)
- [How to run the project](#how-to-run-the-project)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
___
## Project Description

Developing a convenient online store with a wide range of products, secure payments, and easy order management.

Key Features:

   - User-friendly interface and product catalog.
   - Secure payments and account management.
   - Simple cart and order tracking.

***Our goal is to create a reliable platform for pleasant and secure online shopping experiences.***
___
## How to run the project

### *Using Docker*
Using Docker
To run the project with Docker, make sure [Docker](https://www.docker.com/) is installed on your system, then follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/KroshkaByte/store-server.git
    ```
2. Navigate to the project directory:
    ```sh
    cd store-server
    ```
3. [Configure .env](#environment-configuration)

4. Start the project:
    ```sh
    docker-compose up -d --build
    ```

### *Deploying Locally*


Before starting the project setup, ensure that you have the following installed and running on your machine:

>- **Redis**: This project utilizes Redis as a message broker. Ensure Redis is installed and running on your machine. You can download it from [here](https://redis.io/).
>- **PostgreSQL**: The project uses PostgreSQL as the database. Install and configure PostgreSQL on your machine. You can download it from [here](https://www.postgresql.org/).
>- **Stripe CLI**: The quickest way to develop and test webhooks locally is with the Stripe CLI.

As a first step, follow the install guide for [Stripe CLI](https://stripe.com/docs/stripe-cli).

Once you have the Stripe CLI installed and have completed the login process, you’re ready to move on to the next step.

After installing Stripe CLI, run the following command in your terminal:
   ```sh
   stripe listen --forward-to 127.0.0.1:8000/webhook/stripe/
   ```
Save the webhook signing secret that is output in the terminal:
   ```sh
   Your webhook signing secret is whsec_ ... (^C to quit)
   ```
Store this secret in your `.env` file as the variable `STRIPE_WEBHOOK_SECRET`.

**Important**: Each time you run the command `stripe listen --forward-to 127.0.0.1:8000/webhook/stripe/`, 
the webhook signing secret **STRIPE_WEBHOOK_SECRET** will change. 

### *Deploying to VPS*

To deploy the project to your VPS (Virtual Private Server), follow these steps:

1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Set Up Stripe Integration and Register Webhook**: Before deployment, ensure you have configured Stripe for handling payments. Visit [Stripe documentation](https://docs.stripe.com/) to set up Stripe integration and obtain necessary API keys and secrets. After deploying your event handler endpoint to production, register your live URL with Stripe. Follow the guide to register a webhook [here](https://docs.stripe.com/webhooks#register-webhook).

3. **Check Docker Availability**: Ensure Docker is installed on your VPS. If Docker is not installed, follow the instructions to install it:

    - For Ubuntu:
      ```sh
      docker --version
      sudo apt update
      sudo apt install docker.io
      ```
   - For other operating systems, refer to [Docker's](https://docs.docker.com/engine/install/) official installation documentation.

4. **Set Up Domain Name and SSL**: Configure your domain name to point to your VPS IP address. Additionally, set up SSL certificates to enable secure HTTPS connections. Modify the `nginx.conf` file included in the project to use your domain name and SSL certificates.

   - For example, you can refer to [this guide](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04) for obtaining a security certificate and domain binding.

5. **Set Up CI/CD Pipeline**: Modify the `main.yml` file in your forked repository to suit your environment and deployment preferences. Ensure it includes necessary steps like installing dependencies, running tests, and deploying to your VPS.

6. **Add Secrets**: In your GitHub repository settings, add any necessary secrets such as database credentials, API keys, or environment variables needed for deployment. These secrets will be securely passed to your CI/CD pipeline during deployment. 

   - For example, you can refer to this [tutorial](https://dev.to/knowbee/how-to-setup-continuous-deployment-of-a-website-on-a-vps-using-github-actions-54im) for setting up continuous deployment using GitHub Actions.

7. **Push Changes to Main Branch**: Once your CI/CD pipeline is configured and secrets are added, push your changes to the main branch of your forked repository. This will trigger the deployment process to your VPS.


___
#### Environment Configuration
You need to manually update this secret in your `.env` file each time it changes.

Additionally, create a `.env` file in the root directory based on the provided `.env.example` or `.env.docker-example`. Fill in your own data and rename the file to `.env`.

Please note that the Django secret key used in the `.env.example` or `.env.docker-example` is just an example. You can generate a new key using the following command:

   ```sh
   from django.core.management.utils import get_random_secret_key
   
   print(get_random_secret_key())
   ```
Once you have Redis, PostgreSQL, Stripe CLI, and your .env file set up, proceed with the following steps to run the project:
___
**Setting Up and Running in a Virtual Environment**

Ensure that your machine has the latest version of **Python** installed (tested with version 3.12).

1. Clone the repository onto the machine from which the service will be run:

    ```sh
    git clone https://github.com/KroshkaByte/store-server.git
    ```

2. Set up a **Python** virtual environment in the project directory:

    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment for **Linux/Unix**:

    ```sh
    source ./venv/bin/activate 
    ```

   For **Windows**, ensure that script execution is allowed in **Powershell**:

    ```sh
    venv\Scripts\activate
    ```

4. With the virtual environment activated, install the required components:

    ```sh
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory with the necessary environment variables following the example in the `.env.sample` file.

6. Execute migrations (from the virtual environment):

    ```sh
    .\manage.py migrate
    ```
7. (Optional) Load sample data for preview:
    ```sh
   ./manage.py loaddata products/fixtures/categories.json && ./manage.py loaddata products/fixtures/products.json
    ```
8. Run Celery:
   ```sh
   celery -A store worker -l INFO
   ```

9. Run the project:

    ```sh
    .\manage.py runserver
    ```

   The test server will start and be accessible at `http://localhost/8000/`.

10. To create a superuser, execute the following command (from the virtual environment) and follow the prompts:

    ```sh
    python .\manage.py createsuperuser
    ```
___
## Testing

To run the tests, run the following command:
   ```sh
   ./manage.py test . 
   ```
___
## Contributing

   - Fork the repository and create a new branch.
   - Make changes, write tests, and ensure everything works.
   - Commit your changes and submit a PR to the original repository.
   - Provide a clear description in the PR of what you changed and why.

***Thank you for your contribution!***
___
## License

This project is licensed under the MIT License. See the LICENSE file for more information.