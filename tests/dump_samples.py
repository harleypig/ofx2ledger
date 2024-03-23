import yaml
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import OrderedDict

##############################################################################
# YAML Stuff

transact_order = ['name', 'transaction_data', 'expected_output']


#-----------------------------------------------------------------------------
def literal_presenter(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str',
                                       data,
                                       style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


#-----------------------------------------------------------------------------
def dict_representer(dumper, data):
    return dumper.represent_dict(data.items())


#-----------------------------------------------------------------------------
def ordered_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = loader.construct_pairs(node, deep=deep)

    sorted_mapping = sorted(mapping,
                            key=lambda k: transact_order.index(k[0])
                            if k[0] in transact_order else len(transact_order))

    return OrderedDict(sorted_mapping)


#-----------------------------------------------------------------------------
yaml.add_representer(str, literal_presenter)
yaml.add_representer(OrderedDict, dict_representer)

#-----------------------------------------------------------------------------
yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                     ordered_mapping,
                     Loader=yaml.SafeLoader)

##############################################################################
# Jinja Stuff

#-----------------------------------------------------------------------------
env = Environment(loader=FileSystemLoader(
    os.path.join(os.path.dirname(__file__), '..')),
                  autoescape=select_autoescape(['html', 'xml', 'j2']),
                  lstrip_blocks=False,
                  trim_blocks=False)

transact_template = env.get_template('transaction.j2')

samples_j2 = """---
{% for sample_str in sample_strs -%}
{{ sample_str }}
{% if not loop.last %}

{%- endif %}
{%- endfor %}
"""

dump_template = env.from_string(samples_j2)


#-----------------------------------------------------------------------------
def render_transaction(transaction_data):
    rendered = transact_template.render(transaction=transaction_data,
                                        indent='  ').strip()
    return rendered


##############################################################################
# Main

with open('transaction_samples.yaml', 'r') as fh:
    samples = yaml.safe_load(fh)

for sample in samples:
    sample['expected_output'] = render_transaction(sample['transaction_data'])

sample_strs = [
    yaml.dump([sample],
              default_flow_style=False,
              allow_unicode=True,
              sort_keys=False) for sample in samples
]

new_samples = dump_template.render(sample_strs=sample_strs).strip()

with open('temp.yaml', 'w') as fh:
    fh.write(new_samples)
#    yaml.dump(samples, fh,
#              default_flow_style=False,
#              allow_unicode=True,
#              sort_keys=False)
