# CMS (Content Management System)
![cms](https://arjunsingh.com.np/images/portfolio/cms.png)

Something like WordPress but in python. Batteries included CMS with everything that you may need to host a complete website for blog, news, magazines or anything similar.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)

## Features
* Customizable Homepage
* Posts
* Comments
* Users
* Pages
* Categories
* Tags 
* Ads
* Menu (Top, Main, Bottom)
* Scalable
* Mobile Responsive
* Fast
* Different dashboard for users and admin

## Usage
1. First, clone this project,
    ```sh
    git clone https://github.com/mearjunsingh/cms.git
    ```
---
2. Then get inside that folder,
    ```sh
    cd cms
    ```
---
3. Now make sure you have python installed. It is a best practice to install Python projects in a Virtual Environment. To install and create Virtual Envronment,
    ```sh
    pip install virtualenv
    virtualenv venv
    ```
---
4. Now activate virtualenv,
   - In windows
       ```bat
       venv\Scripts\activate
       ```
   - In Linux
        ```sh
        source venv/bin/activate
        ```
---
5. Then install dependencies. To do that,
    ```sh
    pip install -r requirements.txt
    ```
---
6. Now we are ready to run the project. But before that, you must migrate all migrations. Here is how,
    ```sh
    python manage.py migrate
    ```
---
1. You can add superuser by,
    ```sh
    python manage.py createsuperuser
    ```
    *This step is optional but remember, lot of features are only available for superuser.*
---
8. Finally, ready to run the project. Run this command,
    ```sh
    python manage.py runserver
    ```
---
9. Then locate http://127.0.0.1:8000/ in your favorite web browser.
---

## Contributing for project
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
