import os

fs_global = []
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
        title = dn.replace('_', '-')
        f.write(f'# {title}\n\n')
        f.write(s+'\n\n')
    fs_global.append(f'[![{title}]({dn}/0.jpg)]({dn})')

fn = 'README.md'
with open(fn, 'r', encoding='utf-8') as f:
    s = f.read()
pt = '# 预览'
p = s.find(pt)
if p > 0:
    s = s[:p]
s += pt+'\n\n'
s += ' '.join(fs_global)
with open(fn, 'w', encoding='utf-8') as f:
    f.write(s+'\n\n')
