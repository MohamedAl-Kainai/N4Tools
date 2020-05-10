import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="N4Tools",
    version="1.1",
    author="Example Author",
    author_email="mohammedkainaiahmaed@gmail.com",
    description="Style for ( Termux & Kali ) tools...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/No-Name-404/N404-Tool",
    packages=['N4Tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
