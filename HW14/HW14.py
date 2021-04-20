import glob
import time
from concurrent.futures import ThreadPoolExecutor

'Create a script that should find the lines by provided pattern in the provided '
'path directory with recursion (it means if the directory has other directories, '
'the script should get all the info from them as well) and threads.'


def find_by_patter(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_by_pattern(directory_path, pattern):
    files = glob.glob(f'{directory_path}**/*.py', recursive=True)
    container = set()
    with ThreadPoolExecutor() as pool:
        result = pool.map(find_by_patter, files, pattern * len(files))
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    path = 'D:\\PythonProjects\\Cursor\\cursor_hw'
    search_by_pattern = find_all_by_pattern(path, pattern=['import'])
    end = time.time() - start
    for line in search_by_pattern:
        print(line)
    print(f'Search time = {end} seconds')
