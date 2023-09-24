#!/usr/bin/env python3

# https://financialdataexchange.org/common/Uploaded%20files/OFX%20files/OFX%20Banking%20Specification%20v2.3.pdf
# 11.13.1.1.2 Bank Message Set Response Messages
# 11.13.1     Example: Statement Download

# ??? Does MACU have an api token so I can automate downloading my ofx files?

from ofxtools.Parser import OFXTree
#from pprint import pprint

class OFX2Ledger:
    """
    A class to parse an OFX file and provide unique values for a given key.

    This class takes a filename as an argument, parses the OFX file, and saves
    the parsed output to self.ofx. It provides a method to get a list of unique
    values for a given key in the OFX object.

    Attributes:
        ofx (OFX): The parsed and converted OFX object.
    """

    #-------------------------------------------------------------------------
    def __init__(self, ofx_file):
        """
        Initialize the OFX2Ledger object.

        This method calls the _parse_ofx_file method to parse the given OFX file
        and convert it to an OFX object.

        Args:
            ofx_file (str): The path to the OFX file to parse.
        """
        self.ofx = self._parse_ofx_file(ofx_file)

    #-------------------------------------------------------------------------
    def _parse_ofx_file(self, ofx_file):
        """
        Parse the given OFX file and convert it to an OFX object.

        This method attempts to parse the given OFX file and convert it to an
        OFX object. If the parsing or conversion fails, it will raise an exception
        with an appropriate error message and the exception details.

        Args:
            ofx_file (str): The path to the OFX file to parse.

        Returns:
            OFX: The parsed and converted OFX object.
        """
        try:
            # Parse the OFX file
            parser = OFXTree()
            parser.parse(ofx_file)

            # Convert the tree to an OFX object
            ofx = parser.convert()

            if not ofx.bankmsgsrsv1:
                raise ValueError("DEBUG: Expected to find BANKMSGSRSV1 but it's not there.")

            return ofx

        except ValueError as ve:
            raise ValueError(f"Failed to parse OFX file: {ofx_file}. Exception: {ve}")

        except Exception as e:
            raise Exception(f"Failed to parse OFX file: {ofx_file}. Exception: {e}")

    #-------------------------------------------------------------------------
    def get_unique_accounts(self):
        """
        Get a list of unique account ids and types in the OFX object.

        This method iterates over the statements in the OFX object and adds the
        account id and type to a set, effectively collecting all unique account ids
        and types.

        Returns:
            list: A list of tuples, where each tuple contains a unique account id
            and type in the OFX object.
        """
        unique_accounts = set()

        for statement in self.ofx.statements:
            unique_accounts.add((statement.acctid, statement.accttype))

        return list(unique_accounts)

#-----------------------------------------------------------------------------
