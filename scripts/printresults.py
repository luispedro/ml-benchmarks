import re
from glob import glob
pat = re.compile('(?P<name>[A-Za-z.]+): mean (?P<mean>[0-9.e+-]+), std (?P<std>[0-9.e+-]+)$')

benchmarks = [b[:-len('.txt')] for b in glob('*.txt')]

packages = set()

values = {}
for bench in benchmarks:
    values[bench] = {}
    for line in file('%s.txt' % bench):
        m = pat.match(line)
        if m:
            res = m.groupdict()
            name = res['name']
            values[bench][name] = float(res['mean'])
            packages.add(name)

formatstr = '%16s'
print formatstr % '',
for p in packages:
    print formatstr % p,
print
for bench in benchmarks:
    print formatstr % bench,
    minval = min(values[bench].values())
    for p in packages:
        v = values[bench].get(p)
        if v is None:
            print formatstr % '--',
        elif v == minval:
            print formatstr % '1.0**',
        else:
            v /= minval
            print formatstr % ('%.2f' % v),
    print

print
print
print "Results are displayed as relative to the fastest system."
print "Therefore the fastest system always takes 1.0"
print
