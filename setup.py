try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name' : 'Iris',
    'description': 'K Nearest Neighbors labelling of classic iris dataset.',
    'author': 'Cooper Stimson',
    'author_email': 'cooper@cooperstimson.com',
    'url': 'github.com/6c1/iris',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['iris'],
}

setup(**config)
