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
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    {'date': '2023-04-01', 'status': '!', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    {'date': '2023-04-01', 'code': 'INV123', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    {'date': '2023-04-01', 'description': 'Invoice Payment', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    {'date': '2023-04-01', 'tags': {'Payee': 'Client A'}, 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    {'date': '2023-04-01', 'comments': ['Payment received'], 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD'}]},
    # All possible combinations of postings with minimal transaction line
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD', 'status': '!'}]},
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD', 'tags': {'Category': 'Income'}}]},
    {'date': '2023-04-01', 'postings': [{'account_name': 'Assets:Bank', 'amount': '100 USD', 'comments': ['Deposit']}]}
])
def test_transaction_template(transaction_data):
    result = render_transaction(transaction_data)
    assert isinstance(result, str)
    assert '2023-04-01' in result
    assert 'Assets:Bank' in result
    assert '100 USD' in result
    if 'status' in transaction_data:
        assert transaction_data['status'] in result
    if 'code' in transaction_data:
        assert transaction_data['code'] in result
    if 'description' in transaction_data:
        assert transaction_data['description'] in result
    if 'tags' in transaction_data:
        for key, value in transaction_data['tags'].items():
            assert f"{key}: {value}" in result
    if 'comments' in transaction_data:
        for comment in transaction_data['comments']:
            assert comment in result
    for posting in transaction_data['postings']:
        if 'status' in posting:
            assert posting['status'] in result
        if 'tags' in posting:
            for key, value in posting['tags'].items():
                assert f"{key}: {value}" in result
        if 'comments' in posting:
            for comment in posting['comments']:
                assert comment in result
