
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colruytscraper',
    version='0.1',
    author="Simon Gulix",
    description="Collecting product information from Belgian supermarket: Colruyt",
    long_description=long_description,
    install_requires=[
        'requests'
    ],
    long_description_content_type="text/markdown",
    url="https://github.com/SimonGulix/colruyt_scraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
