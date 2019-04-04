from setuptools import setup, find_packages

setup(
    name='abcd',
    version='0.4',
    author='Adam Fekete, Gabor Csanyi',
    author_email='adam.fekete@kcl.ac.uk',
    description='This is an package witch help to store and share atomistic data.',
    keywords='ase, database, mongo, flask',
    url='https://fekad.github.io/abcd/',  # project home page, if any
    project_urls={
        'Documentation': 'https://fekad.github.io/abcd/',
        'Source Code': 'https://github.com/fekad/abcd',
    },
    packages=find_packages(),
    # install_requires=['ase', 'click', 'ply'],
    install_requires=['ase', 'click', 'ply', 'mongoengine', 'blinker', 'tabulate', 'requests', 'numpy', 'dominate'],
    extras_require={
        'mongo': ['mongoengine', 'blinker'],
        'http': ['requests'],
        'server-api': ['flask'],
        'server-app': ['flask', 'Flask-Nav', 'Flask-MongoEngine', 'gunicorn'],
    },
    entry_points={
        'console_scripts': ['abcd=abcd.frontends.shell:cli']
    },
)