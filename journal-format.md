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

## [Transactions](https://hledger.org/hledger.html#default-commodity)

[date](https://hledger.org/hledger.html#dates) [\[null\|\!\|\*\]](https://hledger.org/hledger.html#status) [\[(code)\]](https://hledger.org/hledger.html#code) [\[description\]](https://hledger.org/hledger.html#description) \[\<indent\>; [transaction comment](https://hledger.org/hledger.html#account-comments) \| [tag](https://hledger.org/hledger.html#tags-1) ...\]
\[\<indent\>; [transaction comment](https://hledger.org/hledger.html#account-comments) continued \| [tag](https://hledger.org/hledger.html#tags-1) ...\]\*
; [posting](https://hledger.org/1.26/hledger.html#virtual-postings)
\<indent\> [\[null\|\!\|\*\]](https://hledger.org/hledger.html#status) [account name](https://hledger.org/hledger.html#account-names) \[\<indent\>[amount](https://hledger.org/hledger.html#amounts)\] \[\<indent\>; [posting comment](https://hledger.org/hledger.html#comments) \| [tag](https://hledger.org/hledger.html#tags-1) ...\]
\[\<indent\>; [posting comment](https://hledger.org/hledger.html#comments) continued \| [tag](https://hledger.org/hledger.html#tags-1) ...\]\*
