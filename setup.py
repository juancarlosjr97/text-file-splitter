
from setuptools import setup, Extension
from os import path


def get_version():
    return "0.0.12"


this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="text-file-splitter",
    packages=["text_files_splitter"],
    version=get_version(),
    description="Python module to split files fast and easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Juan Carlos Blanco Delgado",
    author_email="juancarlosjr97@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    license='MIT',
    url="https://github.com/juancarlosjr97/text-file-splitter",
    download_url=f"https://github.com/juancarlosjr97/text-file-splitter/dist/text-file-splitter-{get_version()}.tar.gz",
    keywords="csv split splitter"
)
