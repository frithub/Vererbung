class FileReader():
    def __init__(self, filename):
        self.filename = filename

    def lines(self):
        lines = []
        with open(self.filename, "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines


class CsvReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def lines(self):
        lines = super().lines()

        return [line.split(",") for line in lines]
        # lines_splitted = []
        # for line in lines:
        #    lines_splitted.append(line.split(","))
        # return lines_splitted

f = FileReader("./datei.csv")
print(f.lines())

f = CsvReader("./datei.csv")
print(f.lines())