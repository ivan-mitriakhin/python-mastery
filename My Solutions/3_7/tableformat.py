from abc import ABC, abstractmethod

# Strategy design pattern
# Define an abstract base class and various handler subclasses
# Pass those objects to other classes as attributes or to functions
# as arguments and the behavior of those classes and functions is
# going to vary based on which handler subclass is actually used.

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass
    
    @abstractmethod
    def row(self, rowdata):
        pass

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
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')
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

