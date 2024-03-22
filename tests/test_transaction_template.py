import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml
from yaml.representer import SafeRepresenter
import yaml
import os

def literal_presenter(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, literal_presenter)

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml', 'j2']),
    lstrip_blocks=False,
    trim_blocks=False
)
                  autoescape=select_autoescape(['html', 'xml', 'j2']))

def load_samples():
    with open(os.path.join(os.path.dirname(__file__), 'transaction_samples.yaml'), 'r') as file:
        samples = yaml.safe_load(file)
    return samples

def render_transaction(transaction_data):
    template = env.get_template('transaction.j2')
    return template.render(transaction=transaction_data, indent='  ').strip()

@pytest.mark.parametrize("sample", load_samples())
def test_transaction_template(sample):
    transaction_data = sample['transaction_data']
    expected_output = sample['expected_output']
    result = render_transaction(transaction_data)
    assert isinstance(result, str)
    assert result == expected_output
