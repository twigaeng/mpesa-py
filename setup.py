import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mpesa-py",
    version="0.0.4",
    author="Aurlus Ismael Wedava",
    author_email="arlusishmael@gmail.com",
    description="A Python wrapper for Mpesa Daraja APIs.",
    long_description="This library provides thin wrappers around Mpesa Daraja APIs. The APIs supported are Reversal, Transaction Status, Account Balance, B2B, B2C, C2B and MPESA Express",
    url="https://github.com/Arlus/mpesa-py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'certifi', 'chardet', 'future', 'idna', 'requests',
        'six', 'urllib3', 'pytest'
    ],
)
