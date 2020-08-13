import os

for dn in os.listdir():
    if not os.path.isdir(dn):
        continue
    fs = []
    for fn in os.listdir(dn):
        if not fn.endswith('.jpg'):
            continue
        fs.append(fn)
    fs.sort()
    s = []
    for fn in fs:
        name, _ = fn.split('.')
        ds = f'![{name}]({name}.jpg)'
        s.append(ds)
    s = ' '.join(s)
    fn = os.path.join(dn, 'README.md')
    with open(fn, 'w', encoding='utf-8') as f:
        dn = dn.replace('_', '-')
        f.write(f'# {dn}\n\n')
        f.write(s+'\n\n')
