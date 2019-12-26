# enrollment App

Simple webapp using flask microframework that enrolls people for some courses.

# App structure
```bash
|-- application
|   |-- __init__.py
|   |-- routes.py
|   |-- forms.py
|   |-- models.py
|   |-- static
|       |-- css
|       |-- images
|   |-- templates
|       |-- html files
|-- .flaskenv
|-- config.py
|-- main.py
|-- requirements.txt
|-- venv
```

# How to run
```bash
virtualenv venv
source venv/bin/activate
flask run
```


# CI: How to auto test on travis perhaps