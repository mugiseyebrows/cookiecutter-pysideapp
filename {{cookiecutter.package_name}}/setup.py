from setuptools import setup, find_packages

try:
    with open('readme.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    packages = find_packages(),
    name = "{{cookiecutter.package_name}}",
    version = "0.0.1",
    author = "{{cookiecutter.author}}",
    author_email = "{{cookiecutter.author_email}}",
    url = "{{cookiecutter.url}}",
    description = "{{cookiecutter.description}}",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
{% if cookiecutter.flavour == "pyside6" %}
    install_requires = ['PySide6'],
{% elif cookiecutter.flavour == "pyqt5" %}
    install_requires = ['PyQt5'],
{% endif %}
    entry_points = {
        'gui_scripts': [
            '{{cookiecutter.package_name}} = {{cookiecutter.package_name}}:main'
        ]
    }
)