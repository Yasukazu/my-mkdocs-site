# - generate new post: 1st argument is title, later ones are tags
# - title is slugified into the filename of the post
import sys, datetime, os, yaml, regex
from slugify import slugify
# from pathvalidate import sanitize_filename
# from jinja2 import Template
hira_kata = regex.compile(r"\p{Hiragana}+|\p{Katakana}+|\p{Han}+|\p{posix_alnum}+")
# charkind_ranges = lambda title: [slice(x.start(), x.end()) for x in hira_kata.finditer(title)]

def split_charkind(text):
	list = []
	for x in hira_kata.finditer(text):
		list.append(text[x.start(): x.end()])
	return list

posts_dir = os.path.join('docs', 'posts')
if not os.path.isdir(posts_dir):
	sys.exit(f"{posts_dir} does not exist!")

if len(sys.argv) <= 1:
	print('New post generator. Needs at least 1 argument as the title, later ones become tags.')
	sys.exit(1)
#node = '-'.join([n for n in sys.argv[1:]])
# output = io.StringIO()

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
args = sys.argv[1:]
title = args[0]
tags = args[1:]
# print('title: ' + title, file=output)
today = datetime.date.today()
meta = {'title': title, 'date': today, 'tags': tags}
front_mat = yaml.dump(meta, allow_unicode=True).replace('\n-', '\n -')
# print(HR, file=output) print(front_mat, file=output) print(HR, file=output)
header = '\n'.join([HR, front_mat, HR]) # output.getvalue()
slug = slugify(' '.join(split_charkind(title)), stopwords=['the', 'a'])
filespec = os.path.join(posts_dir, slug + '.md')
with open(filespec, 'w', encoding='utf-8') as out:
	print(header, file=out)

if os.path.exists(filespec):
	print('Following file is created.')
	print(filespec)
else:
	print('Following file is not created!')
	print(filespec)
	sys.exit(3)
"""
def slugify(cc: str):
	cc = cc.strip().rstrip() # remove leading and trailing spaces
	# nodes = cc.split(' ')
	# output = io.StringIO()
	# for n in nodes:
		# print(''.join([c.lower() if c.isalnum() else '-' for c in n]), file=output, end='_')
	return  sanitize_filename(cc).lower().replace(' ', '-')
	# return output.getvalue().rstrip('_').rstrip('-')
"""