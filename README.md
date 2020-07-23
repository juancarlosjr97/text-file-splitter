# Text File Splitter

[![CircleCI](https://img.shields.io/circleci/build/github/juancarlosjr97/text-file-splitter/master?token=4c2bb611baecd30d6be4a947f488dc8791ffa92d)](https://img.shields.io/circleci/build/github/juancarlosjr97/text-file-splitter/master?token=4c2bb611baecd30d6be4a947f488dc8791ffa92d)
[![Issues](https://img.shields.io/github/issues/juancarlosjr97/text-file-splitter)](https://img.shields.io/github/issues/juancarlosjr97/text-file-splitter)
[![Forks](https://img.shields.io/github/forks/juancarlosjr97/text-file-splitter)](https://img.shields.io/github/forks/juancarlosjr97/text-file-splitter)
[![License](https://img.shields.io/github/license/juancarlosjr97/text-file-splitter)](https://img.shields.io/github/license/juancarlosjr97/text-file-splitter)
[![Stars](https://img.shields.io/github/stars/juancarlosjr97/text-file-splitter)](https://img.shields.io/github/stars/juancarlosjr97/text-file-splitter)

Python module to split text file easy and fast, without compromising memory using big files.

## Installation

You can install text-file-splitter by running the following command:

    pip install text-file-splitter

Or you can download direct from [Github](https://github.com/juancarlosjr97/text-file-splitter) and install it manually.

## Usage

Import the module and initialise it.

```python
    from text_files_splitter import TextFilesSplitter, ListMetrics

    source_file = './src/test/files'
    file_name = 'test_csv.csv'
    max_size_file = 10
    file_type = 'csv' # Optional - default 'csv'
    metric_units = ListMetrics.MB # Optional - default ListMetrics.B
    output_directory = './output' # Optional - default the current directory
    include_header = True # Optional - default True
    file_suffix = 'file_example' # Optional - default file_name

    file_splitter = TextFilesSplitter(source_file, file_name, max_size_file, file_type,
                                                ListMetrics.MB, output_directory, include_header, file_suffix)

    files_splitted = file_splitter.get_file_splitted()
```

The outcome of `get_file_splitted()` is a list of dict with the following details

```
files_splitted = [
    {
        "file_name": file_name,
        "path": output_directory,
        "file_size": file_size_in_bytes,
        "count": count
    }...
]


```

## Files compatibility

- csv

## Test

To run a test of the clone the repository and follow the instructions

    pip install test-requirements.txt
    python -m src.test.test

### Expected Outcome

the time may vary depending on your machine performance

```
Ran 1 test in 0.180s

OK
```

### List of test created

- csv

## Requirements

- Python 3.4 or newer

## Code Standards

Following pylint standards

## License

The MIT License (MIT). Please see [License File](https://github.com/juancarlosjr97/text-file-splitter/blob/master/LICENSE.md) for more information.

## Contributions
