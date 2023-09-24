import os

##############################################################################
class Ledger:
    """
    A class to get information about ledger files.

    This class takes an optional filename as an argument and sets it to
    self.filename.  If no filename is passed, it checks for
    DEFAULT_MAIN_LEDGER and sets filename to that, otherwise it raises a ValueError.

    Attributes:
        filename (str): The path to the ledger file.
    """

    DEFAULT_MAIN_LEDGER = os.path.expanduser("~/.hledger.journal")

    def __init__(self, filename=DEFAULT_MAIN_LEDGER):
        """
        Initialize the Ledger object.

        This method sets the filename attribute. If no filename is passed, it
        checks for DEFAULT_MAIN_LEDGER and sets filename to that, otherwise
        it raises a ValueError.

        Args:
            filename (str, optional): The path to the ledger file. Defaults to DEFAULT_MAIN_LEDGER.
        """
        if os.path.exists(filename):
            self.filename = filename
        else:
            raise ValueError(f"File {filename} does not exist.")
