#!/usr/bin/env python3
from ofx2ledger.ofx import OFX2Ledger

if __name__ == "__main__":
    #ofx_file = sys.argv[1]
    #csv_file = sys.argv[2]
    #ofx_file = 'test.ofx'
    ofx_file = 'raw/AllMACUAccounts_2022.ofx'
    ofx2ledger = OFX2Ledger(ofx_file)
    print(ofx2ledger.get_unique('ACCTID'))
