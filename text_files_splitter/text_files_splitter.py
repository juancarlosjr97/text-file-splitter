import os
import re


class BytesMultiples:
    DECIMAL = 1000
    BINARY = 1024


def get_exp_by_metric(metric_unit):
    metric = {
        'B': 0,
        'K': 1,
        'M': 2,
        'G': 3,
        'T': 4,
        'P': 5
    }

    return metric[metric_unit]


def remove_file(file_name):
    os.remove(file_name)


def get_file_size_bytes(file_name):
    return os.path.getsize(file_name)


def get_file_size_metric(file_bytes, metric=get_exp_by_metric('B'), bytes_multiples=BytesMultiples.DECIMAL):

    total_divisions = metric[1]
    file_size_metric = file_bytes

    while total_divisions:
        file_size_metric /= bytes_multiples
        total_divisions -= 1

    return file_size_metric


def get_size_to_metric(size, metric):

    while metric:
        size *= BytesMultiples.DECIMAL
        metric -= 1

    return size


def get_total_file_splits(file_bytes, file_size_limit):

    splits = file_bytes / file_size_limit
    return int(splits) if splits.is_integer() else int(splits) + 1


def delete_file_last_row(file):
    file_rows_exceeded_size = open(file, 'r+').readlines()
    file_rows_exceeded_size.pop()

    file_finished = open(file, 'w+')
    file_finished.writelines(file_rows_exceeded_size)


def get_file_name_splitted(file_suffix, split_count):
    return '{}_{}.csv'.format(file_suffix, split_count)


def create_file_splitted(output_directory, file_splitted_name):
    file_path = os.path.join(output_directory, file_splitted_name)
    return open(file_path, 'w')


class TextFilesSplitter():
    def __init__(self, file_path, max_size_file, file_type='csv', output_directory='.', include_header=True, file_suffix=None):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.max_size_file = int(re.search(r'\d+', max_size_file).group())
        metric_unit = max_size_file.replace(str(self.max_size_file), '')
        self.metric_units = get_exp_by_metric(metric_unit)

        if not os.path.isdir(output_directory):
            os.mkdir(output_directory)

        self.output_directory = output_directory
        self.include_header = include_header
        self.file_suffix = file_suffix

        self.file_suffix = file_suffix or self.file_name

    def append_new_file(self, file_size, count):
        self.splitted_files.append({
            "file_name": self.file_splitted_name,
            "path": self.output_directory,
            "file_size": file_size,
            "count": count
        })

    def get_file_splitted(self):

        self.splitted_files = []

        self._buffer = 1000000

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(
                'The file {} does not exist.'.format(self.file_path))

        file_size_limit = get_size_to_metric(
            self.max_size_file, self.metric_units)

        split_count = 1
        file_to_split = open(self.file_path, 'r')

        header_value = file_to_split.readline()

        file_header = ("".join(header_value))

        file_to_split.seek(0)

        last_row = None
        lines_to_append_file = []
        current_splitted_file_size = 0
        total_size = 0

        def file_splitted_setup(
                current_splitted_file_size, total_size, first_file):
            self.file_splitted_name = get_file_name_splitted(
                self.file_suffix, split_count)
            current_file_splitted = create_file_splitted(
                self.output_directory, self.file_splitted_name)

            if (self.include_header and not first_file):
                size_header = len(file_header)
                current_splitted_file_size += size_header
                total_size += size_header
                current_file_splitted.write("".join(file_header))

            return current_file_splitted, current_splitted_file_size, total_size

        current_file_splitted, current_splitted_file_size, total_size = file_splitted_setup(
            current_splitted_file_size, total_size, True)

        for line in file_to_split:

            size = len(line)
            current_splitted_file_size += size
            total_size += size

            if (last_row):

                current_file_splitted.close()
                current_file_splitted, current_splitted_file_size, total_size = file_splitted_setup(
                    current_splitted_file_size, total_size, False)

                size_last_row = len(last_row)
                current_splitted_file_size += size_last_row
                total_size += size_last_row

                lines_to_append_file.append(last_row)
                last_row = None

            if (current_splitted_file_size <= self._buffer) & (total_size < file_size_limit):
                lines_to_append_file.append(line)
                continue
            elif (current_splitted_file_size > self._buffer) & (total_size < file_size_limit):
                lines_to_append_file.append(line)
                current_file_splitted.write("".join(lines_to_append_file))
                current_splitted_file_size = 0
                lines_to_append_file = []
            else:
                self.append_new_file(total_size, split_count)
                total_size = 0
                current_splitted_file_size = 0
                last_row = "".join(line)
                split_count += 1

        if (lines_to_append_file):
            self.append_new_file(current_splitted_file_size, split_count)
            current_file_splitted.write("".join(lines_to_append_file))
            current_file_splitted.close()

        file_to_split.close()

        return self.splitted_files
