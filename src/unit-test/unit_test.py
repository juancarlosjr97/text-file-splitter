#!/usr/bin/env python

from src.text_files_splitter.text_files_splitter import TextFilesSplitter, ListMetrics
import unittest


class TestStringMethods(unittest.TestCase):

    def test_csv(self):
        source_file = './src/unit-test/files'
        file_name = 'test_csv.csv'
        max_size_file = 10
        file_type = 'csv'  # Optional - default 'csv'
        metric_units = ListMetrics.MB  # Optional - default ListMetrics.B
        output_directory = './output'  # Optional - default the current directory
        include_header = True  # Optional - default True
        file_suffix = 'file_example'  # Optional - default file_name

        file_splitter = TextFilesSplitter(
            source_file=source_file,
            file_name=file_name,
            max_size_file=max_size_file,
            file_type=file_type,
            metric_units=metric_units,
            output_directory=output_directory,
            include_header=include_header,
            file_suffix=file_suffix
        )

        files_splitted = file_splitter.get_file_splitted()

        self.assertEqual(len(files_splitted), 4)


if __name__ == "__main__":
    unittest.main()
