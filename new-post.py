import sys, datetime, os, io

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
print('---', file=output)
def slugify(cc: str):
	cc = cc.strip().rstrip()
	nodes = cc.split(' ')
	output = io.StringIO()
	for n in nodes:
		print(''.join([c if c.isalnum() else '-' for c in n]), file=output, end='_')
	return output.getvalue().rstrip('_')
breakpoint()
args = [n for n in sys.argv[1:]]
title = ' '.join(args)
print('title: ' + title, file=output)
iso=datetime.datetime.now().isoformat()
today=iso[0 : iso.index('T')]
print("date: " + today, file=output)
print('---', file=output)
header = output.getvalue()
slugs = [slugify(n) for n in args]
node = '_'.join(slugs)
filespec = os.path.join(posts_dir, node + '.md')
breakpoint()
with open(filespec, 'w') as output:
	print(header, output=output)
print(filespec + ' is created.')
