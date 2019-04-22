# Dictionary Cleaner
Recursive function to remove keys in two dictionaries in Python

Use case: removing fields from dictionaries prior to using deepdiff

## Requirements
 - Python 3

## Usage
Example: Remove key "bar" and associated values (if they exist) in either of two dictionaries.
```
import cleaner

cleaner.remove_keys({"foo":123}, {"foo":123, "bar":456}, {"bar":True})
```
