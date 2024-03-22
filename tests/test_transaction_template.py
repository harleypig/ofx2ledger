import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader('path/to/your/templates'),
                  autoescape=select_autoescape(['html', 'xml', 'j2']))


@pytest.mark.parametrize(
    "transaction_data, expected_output",
    [
        # All possible combinations of transaction with minimal posting entry
        ({
            'date': '2023-04-01',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "2023-04-01\n\n  Assets:Bank  100.00\n"),
        ({
            'date': '2023-04-01',
            'status': '!',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "2023-04-01 !\n\n  Assets:Bank  100.00\n"),
        ({
            'date': '2023-04-01',
            'code': 'INV123',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "2023-04-01 INV123\n\n  Assets:Bank  100.00\n"),
        ({
            'date': '2023-04-01',
            'description': 'Invoice Payment',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "string"),
        ({
            'date': '2023-04-01',
            'tags': {
                'Payee': 'Client A'
            },
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "string"),
        ({
            'date': '2023-04-01',
            'comments': ['Payment received'],
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00'
            }]
        }, "string"),

        # All possible combinations of postings with minimal transaction line
        ({
            'date':
            '2023-04-01',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00',
                'status': '!'
            }]
        }, "string"),
        ({
            'date':
            '2023-04-01',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00',
                'tags': {
                    'Category': 'Income'
                }
            }]
        }, "string"),
        ({
            'date':
            '2023-04-01',
            'postings': [{
                'account_name': 'Assets:Bank',
                'amount': '100.00',
                'comments': ['Deposit']
            }]
        }, "string")
    ])
def test_transaction_template(transaction_data, expected_output):
    result = render_transaction(transaction_data)
    assert isinstance(result, str)
    assert result == expected_output


def render_transaction(transaction_data):
    template = env.get_template('transaction.j2')
    return template.render(transaction=transaction_data).strip()
