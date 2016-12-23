

import collections

ct = collections.Counter()
for word in ['red', 'blue','red','green','blue','red']:
    ct[word] += 1

print(ct)