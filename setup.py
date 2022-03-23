from importlib.machinery import SourceFileLoader

import setuptools

install_requirements = [
    'requests>=2.21.0,<3.0.0',
    'dataclasses>=0.6;python_version<"3.7"',
]

version = SourceFileLoader('version', 'botmaker/version.py').load_module()


test_requires = [
    'pytest',
    'pytest-vcr',
    'pytest-cov',
    'black',
    'isort',
    'flake8==3.7.9',
    'mypy==0.812',
]

with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name='botmaker',
    version=version.__version__,
    author='Cuenca',
    author_email='dev@cuenca.com',
    description='BotMaker API Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cuenca-mx/botmaker-python',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=install_requirements,
    setup_requires=['pytest-runner'],
    tests_require=test_requires,
    extras_require=dict(test=test_requires),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
