from setuptools import setup, find_packages

setup(
    name='myapp',  # Replace with your app name
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=5.1.7',
        'requests>=2.32.3',
        'behave>=1.2.6',
        'django-behave>=0.1.6',  # if you plan to integrate behave with Django
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',  # for running tests with pytest
            'pytest-django>=4.4.0',  # for Django testing with pytest
        ],
    },
    test_suite='nose.collector',  # You can use unittest, pytest, or behave
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
