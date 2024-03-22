import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('path/to/your/templates'),
    autoescape=select_autoescape(['html', 'xml', 'j2'])
)

def render_transaction(transaction_data):
    template = env.get_template('transaction.j2')
    return template.render(transaction=transaction_data).strip()

@pytest.mark.parametrize("transaction_data", [
    # All possible combinations of transaction with minimal posting entry
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    {'date': '2023-04-01', 'status': '!', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    {'date': '2023-04-01', 'code': 'INV123', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    {'date': '2023-04-01', 'description': 'Invoice Payment', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    {'date': '2023-04-01', 'tags': {'Payee': 'Client A'}, 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    {'date': '2023-04-01', 'comments': ['Payment received'], 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00'}]},
    # All possible combinations of postings with minimal transaction line
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00', 'status': '!'}]},
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00', 'tags': {'Category': 'Income'}}]},
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100.00', 'comments': ['Deposit']}]}
])

# First entry above should produce this:
# 2023-04-01
#
#   Assets:Bank  100.00

def test_transaction_template(transaction_data, expected_output):
    result = render_transaction(transaction_data)
    assert isinstance(result, str)
    # Check the format of the transaction line
    transaction_line = result.split('\n')[0]
    assert transaction_line.startswith(transaction_data['date'])
    if 'status' in transaction_data:
        assert f" {transaction_data['status']}" in transaction_line
    if 'code' in transaction_data:
        assert f" {transaction_data['code']}" in transaction_line
    if 'description' in transaction_data:
        assert f" {transaction_data['description']}" in transaction_line
    # Check the format of tags and comments
    if 'tags' in transaction_data:
        for key, value in transaction_data['tags'].items():
            assert f"\n  ; {key}: {value}" in result
    if 'comments' in transaction_data:
        for comment in transaction_data['comments']:
            assert f"\n  ; {comment}" in result
    # Check the format of postings
    for posting in transaction_data['postings']:
        posting_line = f"\n  {posting['account_name']}"
        if 'status' in posting:
            posting_line = f"\n  {posting['status']} {posting_line.lstrip()}"
        if 'amount' in posting:
            posting_line += f"  {posting['amount']}"
        assert posting_line in result
        if 'tags' in posting:
            for key, value in posting['tags'].items():
                assert f"\n  ; {key}: {value}" in result
        if 'comments' in posting:
            for comment in posting['comments']:
                assert f"\n  ; {comment}" in result
