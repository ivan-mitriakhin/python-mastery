from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join(f"{h:10s}" for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join(f"{str(d):10s}" for d in rowdata))