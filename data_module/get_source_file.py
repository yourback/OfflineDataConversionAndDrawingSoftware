def get_source_data():
    with open('../temp_data.txt', 'r+') as f:
        while True:
            single_line = f.readline()
            yield single_line


def file_read_lines():
    with open('../temp_data.txt', 'r+') as f:
        lines = f.readlines()

    for single_line in lines:
        yield single_line


if __name__ == '__main__':
    file_read_lines()
