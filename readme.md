# CMS
comming soon.

[More Info Here](https://arjunsingh.com.np/cms)

## Usage

First, clone this project

```bash
git clone https://github.com/mearjunsingh/cms.git
```

Then

```bash
cd cms
```

Now make sure you have python installed. It's best practice to install Python projects in a Virtual Environment. To install and create Virtual Envronment, 

```bash
pip install virtualenv
virtualenv venv
```

Now activate virtualenv,

* In windows
```bash
venv\scripts\activate
```
* In Linux
```bash
source venv/bin/activate
```

Then install dependencies. To do that,

```bash
pip install -r requirements.txt
```

Now we are ready to run the project. But before that, you must migrate all migrations. Here is how,

```bash
python manage.py migrate
```
* [Optional] You can add superuser to access admin area. You can do so by,
```bash
python manage.py createsuperuser
```
Now enter username, email and passwords.

Finally, ready to run the project. Run this command:
```bash
python manage.py runserver
```

Then locate http://127.0.0.1:8000/ in your favorite web browser.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.