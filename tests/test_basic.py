from text_files_splitter.text_files_splitter import TextFilesSplitter
import unittest


class TestStringMethods(unittest.TestCase):

    def test_csv(self):
        file_path = './files/test_csv.csv'
        max_size_file = '10M'
        file_type = 'csv'
        output_directory = './output'
        include_header = False
        file_suffix = 'file_example'

        file_splitter = TextFilesSplitter(
            file_path=file_path,
            max_size_file=max_size_file,
            file_type=file_type,
            output_directory=output_directory,
            include_header=include_header,
            file_suffix=file_suffix
        )

        files_splitted = file_splitter.get_file_splitted()

        self.assertEqual(len(files_splitted), 4)


if __name__ == "__main__":
    unittest.main()
