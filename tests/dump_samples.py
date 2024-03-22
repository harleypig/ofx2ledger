import yaml
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '..')),
                  autoescape=select_autoescape(['html', 'xml', 'j2']))

def render_transaction(transaction_data):
    template = env.get_template('transaction.j2')
    rendered = template.render(transaction=transaction_data, indent='  ').strip()
    return rendered

with open('transaction_samples.yaml', 'r') as file:
    samples = yaml.safe_load(file)

for sample in samples['transaction_samples']:
    sample['expected_output'] = render_transaction(sample['transaction_data'])

with open('temp.yaml', 'w') as file:
    yaml.dump(samples, file, default_flow_style=False, allow_unicode=True)

