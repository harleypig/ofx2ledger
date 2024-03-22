import yaml
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict

transact_order = ['name', 'transaction_data', 'expected_output']

def literal_presenter(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str',
                                       data,
                                       style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


def ordered_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = loader.construct_pairs(node, deep=deep)

    sorted_mapping = sorted(mapping,
                            key=lambda k: transact_order.index(k[0])
                            if k[0] in transact_order else len(transact_order))

    return OrderedDict(sorted_mapping)


yaml.add_representer(str, literal_presenter)
yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                     ordered_mapping,
                     Loader=yaml.SafeLoader)

env = Environment(loader=FileSystemLoader(
    os.path.join(os.path.dirname(__file__), '..')),
                  autoescape=select_autoescape(['html', 'xml', 'j2']),
                  lstrip_blocks=False,
                  trim_blocks=False)

template = env.get_template('transaction.j2')


def render_transaction(transaction_data):
    rendered = template.render(transaction=transaction_data,
                               indent='  ').strip()
    return rendered


with open('transaction_samples.yaml', 'r') as file:
    samples = yaml.safe_load(file)

for sample in samples:
    sample['expected_output'] = render_transaction(sample['transaction_data'])

with open('temp.yaml', 'w') as file:
    yaml.dump(samples,
              file,
              default_flow_style=False,
              allow_unicode=True)
