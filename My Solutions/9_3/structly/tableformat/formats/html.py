from ..formatter import TableFormatter


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr> ' + '</th> '.join(f"<th>{h}" for h in headers) + '</tr>')
    
    def row(self, rowdata):
        print('<tr> ' + '</td> '.join(f"<td>{str(d)}" for d in rowdata) + '</tr>')