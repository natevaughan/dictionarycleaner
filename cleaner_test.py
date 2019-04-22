import cleaner

dict1 = {"foo": 123, "bar": 456}
dict2 = {"foo": 123, "baz": 567}
remove = {"baz": True}

cleaner.remove_keys(dict1, remove)
cleaner.remove_keys(dict2, remove)

assert (dict1["foo"] == 123), "It should preserve key 'foo'"
assert (dict1["bar"] == 456), "It should preserve key 'bar'"
assert (dict2["foo"] == 123), "It should preserve key 'foo'"
assert ("baz" not in dict2), "It should remove key 'baz'"
