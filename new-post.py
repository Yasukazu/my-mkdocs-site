import sys, datetime, os, io, yaml
# from jinja2 import Template

posts_dir = os.path.join('docs', 'posts')
if not os.path.isdir(posts_dir):
	sys.exit(f"{posts_dir} does not exist!")

if len(sys.argv) <= 1:
	print('Needs slug')
	sys.exit(1)
node = '-'.join([n for n in sys.argv[1:]])
output = io.StringIO()

filespec = os.path.join(posts_dir, node + '.md')
# with open(filespec, 'w') as output:
	# print header
'''
template = """---
title: {{ title }}
date: {{ date }}
---
"""
'''
HR = '---'

def slugify(cc: str):
	cc = cc.strip().rstrip()
	nodes = cc.split(' ')
	output = io.StringIO()
	for n in nodes:
		print(''.join([c if c.isalnum() else '-' for c in n]), file=output, end='_')
	return output.getvalue().rstrip('_').rstrip('-')
args = sys.argv[1:]
title = ' '.join(args)
# print('title: ' + title, file=output)
iso=datetime.datetime.now().isoformat()
date=iso[0 : iso.index('T')]
meta = {'title': title, 'date': date}
front_mat = yaml.dump(meta)
print(HR, file=output)
print(front_mat, file=output)
print(HR, file=output)
header = output.getvalue()
slugs = [slugify(n) for n in args]
node = '_'.join(slugs)
filespec = os.path.join(posts_dir, node + '.md')
if os.path.exists(filespec):
	print("It's already exists:")	
	print(filespec)	
	sys.exit(2)

with open(filespec, 'w') as out:
	print(header, file=out)

if os.path.exists(filespec):
	print('Following file is created.')
	print(filespec)
else:
	print('Following file is not created!')
	print(filespec)
	sys.exit(3)