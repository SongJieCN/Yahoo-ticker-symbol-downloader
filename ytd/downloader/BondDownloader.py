from ..SymbolDownloader import SymbolDownloader
from ..symbols.Bond import Bond

from ..compat import unicode

class BondDownloader(SymbolDownloader):
    def __init__(self):
        SymbolDownloader.__init__(self, "Bond")

    def decodeSymbolsContainer(self, symbolsContainer):
        symbols = []
        for row in symbolsContainer:
            ticker = unicode(row.contents[0].string)
            name = row.contents[1].string
            if name is not None:
                name = unicode(name)
            type = row.contents[3].string

            exchange = row.contents[5].string
            if exchange is not None:
                exchange = unicode(exchange)

            symbols.append(Bond(ticker, name, exchange))
        return symbols

    def getRowHeader(self):
        return SymbolDownloader.getRowHeader(self)
