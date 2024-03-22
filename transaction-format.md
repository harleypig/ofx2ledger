# Ledger Entry Template

The ledger entry format looks like the following example:

```
transaction_date transaction_status transaction_code transaction_description ; transaction_comment | transaction_tag ...
  ; transaction_comment | transaction_tag ...
  ; transaction_comment continued | transaction_tag ...

  posting_status posting_account_name posting_amount
  ; posting_comment | posting_tag ...
  ; posting_comment continued | posting_tag ...
```

## Some points to note

* `transaction_date`, `transaction_status`, `transaction_code`,
    `transaction_description`, `transaction_comment`, `transaction_tag`,
    `posting_status`, `posting_account_name`, `posting_amount`, and
    `posting_tag` all need to be variables in the template file and all need
    to have their own methods in `ledger_template.py`.

* `transaction_status`, `transaction_code`, `transaction_description`,
    `transaction_comment`, `transaction_tag`, `posting_status`,
    `posting_amount`, and `posting_tag` are optional.

* If there is a transaction_comment **or** a transaction_tag then it needs to
    be preceded by `indent;`, either immediately after `transaction_description`
    or on each line **before** the posting section (started with
    `posting_status`), where `indent` is a minimum of 2 spaces.

* The pipe shown in the example is not an `or` function. If `transaction_tag`
    exists for that line, *and* a transaction_comment exists, then separate
    the tag and comment with a pipe symbole (`|`).
