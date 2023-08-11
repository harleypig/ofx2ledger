# Hledger Journal Format 

## General Information

* Text appearing in angle brackets (<\>) is required.
* \<indent\> must be a minimum of two spaces and is required if the line it's
  on is being used.
* There can be only one default commodity
* ledgers [secondary dates](https://hledger.org/hledger.html#secondary-dates)
  are supported but not recommended, stick with [posting
  dates](https://hledger.org/hledger.html#posting-dates)

* Multiple account comment lines can be added, but they end at the first posting

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

You can also declare commodities using the [commodity
directive](https://hledger.org/hledger.html#declaring-commodities). Declaring
commodities can help in formatting and conversion rates. It's a way to tell
hledger how to display amounts of this commodity, and what its conversion rate
is to other commodities.

## Transactions

A transaction in hledger is represented as follows:

```plaintext
[date] [status] [(code)] [description]
  ; transaction comment | tag ...
  ; transaction comment continued | tag ...
; posting
  [status] account name [amount]
  ; posting comment | tag ...
  ; posting comment continued | tag ...
```

Each component of the transaction is explained below:

### Date
The date of the transaction. More details can be found [here](https://hledger.org/hledger.html#dates).

### Status
The status of the transaction. It can be null, !, or *. More details can be found [here](https://hledger.org/hledger.html#status).

### Code
The code of the transaction. More details can be found [here](https://hledger.org/hledger.html#code).

### Description
The description of the transaction. More details can be found [here](https://hledger.org/hledger.html#description).

### Transaction Comment
The comment for the transaction. More details can be found [here](https://hledger.org/hledger.html#account-comments).

### Tag
The tag for the transaction. More details can be found [here](https://hledger.org/hledger.html#tags-1).

### Posting
The posting of the transaction. More details can be found [here](https://hledger.org/1.26/hledger.html#virtual-postings).

### Account Name
The name of the account. More details can be found [here](https://hledger.org/hledger.html#account-names).

### Amount
The amount of the transaction. More details can be found [here](https://hledger.org/hledger.html#amounts).

### Posting Comment
The comment for the posting. More details can be found [here](https://hledger.org/hledger.html#comments).
