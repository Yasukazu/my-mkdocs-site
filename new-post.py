import sys, datetime
if len(sys.argv) <= 1:
	print('Needs slug')
	sys.exit(1)
node = sys.argv[1]
filespec = f'docs/posts/{node}.md'
with open(filespec, 'w') as output:
	# print header
	print('---', file=output)
	title = node.replace('-', ' ')
	print('title: ' + title, file=output)
	iso=datetime.datetime.now().isoformat()
	today=iso[0 : iso.index('T')]
	print("date: " + today, file=output)
	print('---', file=output)
print(filespec + ' is created.')
