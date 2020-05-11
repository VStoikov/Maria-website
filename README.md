# Maria-website
Maria's website

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install
```

## Usage

### Generate ERD diagram of Databases
1. Install this packages:
```bash
pip install graphviz
pip install django-extensions
pip install pyparsing pydot
```
2. Add this configuration in settings.py
```python
INSTALLED_APPS = [
	...,
    'django_extensions',
]
...
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}
```
3. Generate .dot extension
```bash
python manage.py graph_models -a > erd.dot
```
4. Convert .dot extension file to .png file
```bash
python manage.py graph_models --pydot -a -g -o erd.png
```
or use [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline) converter.

## Used sources

1. [Django-appointment-and-booking-system](https://github.com/saroarjahan/Django-appointment-and-booking-system).
2. [Django-Invoice-Generator](https://github.com/OmkarPathak/Django-Invoice-Generator).