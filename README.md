# STORE-SERVER

## Table of Contents

- [How to run the project](#how-to-run-the-project)
- [Project Description](#project-description)
- [Contributing](#contributing)
- [License](#license)

### How to run the project

**Setting Up and Running in a Virtual Environment**

Ensure that your machine has the latest version of **Python** installed (tested with version 3.12).

1. Clone the repository onto the machine from which the service will be run:

    ```
    git clone https://github.com/KroshkaByte/store-server.git
    ```

2. Set up a **Python** virtual environment in the project directory:

    ```
    python3 -m venv venv
    ```

3. Activate the virtual environment for **Linux/Unix**:

    ```
    source ./venv/bin/activate 
    ```

   For **Windows**, ensure that script execution is allowed in **Powershell**:

    ```
    venv\Scripts\activate
    ```

4. With the virtual environment activated, install the required components:

    ```
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory with the necessary environment variables following the example in the `.env.sample` file.

6. Execute migrations (from the virtual environment):

    ```
    .\manage.py migrate
    ```
7. (Optional) Load sample data for preview:
    ```
   ./manage.py loaddata products/fixtures/categories.json && ./manage.py loaddata products/fixtures/products.json
    ```

8. Run the project:

    ```
    .\manage.py runserver
    ```

   The test server will start and be accessible at `http://localhost/8000/`.

9. To create a superuser, execute the following command (from the virtual environment) and follow the prompts:

    ```
    python .\manage.py createsuperuser
    ```
   
### Project Description

Developing a convenient online store with a wide range of products, secure payments, and easy order management.

Key Features:

   - User-friendly interface and product catalog.
   - Secure payments and account management.
   - Simple cart and order tracking.

***Our goal is to create a reliable platform for pleasant and secure online shopping experiences.***

### Contributing

   - Fork the repository and create a new branch.
   - Make changes, write tests, and ensure everything works.
   - Commit your changes and submit a PR to the original repository.
   - Provide a clear description in the PR of what you changed and why.

***Thank you for your contribution!***

### License

This project is licensed under the MIT License. See the LICENSE file for more information.
