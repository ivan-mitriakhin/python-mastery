def print_table(records, names):
    print(' '.join(f"{name:10s}" for name in names))
    print(('-'*10 + ' ') * len(names))
    for record in records:
        print(' '.join(f"{str(getattr(record, name)):10s}" for name in names))


# s = Stock(...)
# b = s.sell
# c = s.sell
#
# s.sell(25)
# ==
# b.__func__(b.__self__, 25)