class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join(f"{h:10s}" for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join(f"{str(d):10s}" for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(h for h in headers))
    
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> ' + '</th> '.join(f"<th>{h}" for h in headers) + '</tr>')
    
    def row(self, rowdata):
        print('<tr> ' + '</td> '.join(f"<td>{str(d)}" for d in rowdata) + '</tr>')

def print_table(records, names, formatter):
    formatter.headings(names)
    for r in records:
        rowdata = [getattr(r, name) for name in names]
        formatter.row(rowdata)

def create_formatter(name):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    return formatter_cls()

