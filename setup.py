from setuptools import find_packages, setup

install_requires = [
    'django-oscar>=4.2',
    'wagtail>=7.4',
]

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest-cov>=2.3.1',
    'pytest-django>=3.0.0',
    'pytest-pythonpath>=0.7',
    'pytest>=3.0.3',

    # Linting
    'isort>=4.2.5',
    'flake8>=3.0.3',
    'flake8-blind-except>=0.1.1',
    'flake8-debugger>=3.0.0',
]

setup(
    name='django-oscar-wagtail',
    version='1.0.0',
    description="Integration between Django Oscar and Wagtail",
    long_description=open('README.rst').read(),
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",

    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    python_requires='>=3.10',
    zip_safe=False,
)
