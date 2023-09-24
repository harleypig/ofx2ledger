import os

class Ledger:
    """
    A class to handle ledger files.

    This class takes an optional filename as an argument and sets it to self.filename.
    If no filename is passed, it checks for $HOME/.hledger.journal and sets filename to that,
    otherwise it sets filename to None.

    Attributes:
        filename (str): The path to the ledger file.
    """

    def __init__(self, filename=None):
        """
        Initialize the Ledger object.

        This method sets the filename attribute. If no filename is passed, it checks for
        $HOME/.hledger.journal and sets filename to that, otherwise it sets filename to None.

        Args:
            filename (str, optional): The path to the ledger file. Defaults to None.
        """
        if filename:
            self.filename = filename
        elif os.path.exists(os.path.expanduser("~/.hledger.journal")):
            self.filename = os.path.expanduser("~/.hledger.journal")
        else:
            self.filename = None
