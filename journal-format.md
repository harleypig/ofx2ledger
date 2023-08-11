# Hledger Journal Format

## General Information

Indentation is crucial in hledger transactions. It must be a minimum of two
spaces and is required if the line it's on is being used. Indentation is used
to group related lines together, such as postings with a transaction, or
comments with the thing they are commenting on.

Without proper indentation, hledger might interpret your data differently than
you intended. For more details, refer to the [hledger
documentation](https://hledger.org/hledger.html).

## File comments

These comments can only appear outside of transaction blocks.

A [single line comment](https://hledger.org/hledger.html#comments) can start
with any of [;#*]. Whenever possible, use '#'.

A [multiline comment](https://hledger.org/hledger.html#comment-blocks) starts
with 'comment' and ends with 'end comment'

```
comment

This is a multi-line file comment.
The blank lines are not required.
The keywords 'comment' and 'end comment' are required.

end comment
```

## [Commodity](https://hledger.org/hledger.html#commodity)

In hledger, a commodity is a kind of value that can be counted or measured. It
could be anything like dollars, hours, etc. The [default
commodity](https://hledger.org/hledger.html#default-commodity) is the one that
hledger will assume when it's not specified in the transactions.

Commodities can be declared in two ways: inline in the amount field of
a posting, or with a [commodity
directive](https://hledger.org/hledger.html#declaring-commodities). Declaring
commodities can help in formatting and conversion rates. It's a way to tell
hledger how to display amounts of this commodity, and what its conversion rate
is to other commodities.

Note: There can be only one default commodity.

## Transactions

A transaction in hledger is represented as follows:

```plaintext
date status code description
  ; transaction comment | tag ...
  ; transaction comment continued | tag ...
; posting
  status account name amount
  ; posting comment | tag ...
  ; posting comment continued | tag ...
```

Each component of the transaction is explained below:

### [Date](https://hledger.org/hledger.html#dates)

`Date` is when the transaction occurred. It is usually written in the format
YYYY/MM/DD.

hledger supports [secondary
dates](https://hledger.org/hledger.html#secondary-dates), but it is
recommended to stick with [posting
dates](https://hledger.org/hledger.html#posting-dates).

This is a required component.

### [Status](https://hledger.org/hledger.html#status)

`Status` is the state of the transaction. It can be null, !, or \*. The status
is used to indicate if the transaction is pending (!) or cleared (\*).

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).

### [Code](https://hledger.org/hledger.html#code)

`Code` is a reference number or identifier for the transaction. It is often
used to record check numbers or other reference information.

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).

### [Description](https://hledger.org/hledger.html#description)

`Description` provides more details about the transaction. It is a brief
summary of the transaction's purpose.

This is a required component.

### [Transaction Comment](https://hledger.org/1.30/hledger.html#transaction-comments)

`Transaction Comment` provides additional information or notes for the
transaction. It can be used to add any extra details about the transaction
that are not covered in the description. Note that multiple account comment
lines can be added, but they end at the first posting. Transaction comments
must be indented to be associated with the transaction.

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).
lines can be added, but they end at the first posting.

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).

### [Tag](https://hledger.org/hledger.html#tags-1)

`Tag` is a keyword or label that helps in categorizing transactions. Tags can
be used to group related transactions together for reporting purposes.

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).

### [Posting](https://hledger.org/hledger.html#virtual-postings)

`Posting` records the changes in account balances due to the transaction. Each
transaction must have at least one posting, and each posting affects the
balance of an account. The order of postings in a transaction can affect the
balance calculations, so it's important to maintain the correct order.

This is a required component.

### [Account Name](https://hledger.org/hledger.html#account-names)

`Account Name` is the name of the account affected by the transaction. Account
names are hierarchical, and different levels of the hierarchy are separated by
colons.

This is a required component.

### [Amount](https://hledger.org/hledger.html#amounts)

`Amount` represents the value of the transaction. Amounts can be in any
currency or commodity, and hledger will keep track of each one separately.

This is a required component.

### [Posting Comment](https://hledger.org/hledger.html#comments)

`Posting Comment` provides additional information or notes about the posting.
It can be used to add any extra details about the posting that are not covered
in the account name or amount. Posting comments must be indented to be
associated with the posting.

This component is optional.

## Additional Information

### Balance Assertions and Balance Assignments

Balance assertions and assignments are a crucial part of hledger's journal format. They allow you to specify the expected balance of an account after a transaction, or to assign a balance to an account. For more details, refer to the [hledger documentation on balance assertions and assignments](https://hledger.org/hledger.html#balance-assertions).

### Periodic Transactions

Periodic transactions are a powerful feature of hledger that allow you to automate recurring transactions. They can be used to automatically generate transactions for regular expenses or income, like rent or salary. For more details, refer to the [hledger documentation on periodic transactions](https://hledger.org/hledger.html#periodic-transactions).

### Automated Transactions

Automated transactions are another powerful feature of hledger that can simplify your accounting. They allow you to define rules that automatically generate additional postings whenever a transaction matches certain criteria. For more details, refer to the [hledger documentation on automated transactions](https://hledger.org/hledger.html#automated-transactions).
