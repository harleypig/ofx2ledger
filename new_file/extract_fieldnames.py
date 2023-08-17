import sys
from ofxtools.Parser import OFXTree

def extract_fieldnames(ofx_file):
    # Parse the OFX file
    tree = OFXTree()
    tree.parse(ofx_file)

    # Extract the field names
    fieldnames = []
    for transaction in tree.convert().bank_statements[0].transactions:
        fieldnames.extend(transaction.__dict__.keys())

    # Remove duplicates and return
    return list(set(fieldnames))

if __name__ == "__main__":
    ofx_file = sys.argv[1]
    fieldnames = extract_fieldnames(ofx_file)
    print("Fieldnames:", fieldnames)
