class FileWorking:
    def __init__(self):
        self.work_file = 'file1.txt'
        self.temp_file = 'file2.txt'

    def get_line(self, n: int):
        file = open(self.work_file, 'r')
        res = file.readlines()[n]
        file.close()
        res = res.replace('\n', '')
        return res

    def set_line(self, n: int, line: str):
        file = open(self.work_file, 'r')
        lines = file.readlines()
        lines = list(map(lambda x: x.replace('\n', ''), lines))
        file.close()
        lines[n] = line
        file = open(self.work_file, 'w')
        file.writelines(map(lambda x: x + '\n', lines))
        file.close()

    def set_lines_count(self, n):
        file = open(self.work_file, 'w')
        file.writelines(['\n'] * n)
        file.close()

    def iterate_throw_old(self):
        file = open(self.temp_file, 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            if line != '\n':
                yield line.replace('\n', '')

    def swap_files(self):
        self.work_file, self.temp_file = self.temp_file, self.work_file

    def get_all_lines(self):
        file = open(self.work_file, 'r')
        lines = file.readlines()
        file.close()
        return lines


fw = FileWorking()
