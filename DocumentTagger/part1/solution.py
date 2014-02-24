#! /usr/local/bin/python
import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART

documents = [DIV_COMM, MAG_CART]

# PREPARE OUR REGEXES FOR METADATA SEARCHES #
# we'll use re.compile() here, which allows you to assign a regex pattern
# to a variable. We'll do this for each our metadata fields.
# 
# Also note how we're using paretheses to create two search groups. Looking
# at title_search, see how we use one group to match on the presence of "title:".
# 
# Also, note how in the second group is a named group -- we use ?p<name> .
# 
# Finally, note that we're passing the re.IGNORECASE flag as an optional
# argument to re.compile. We're doing this because it's human beings who create
# the metadata headers at the top of Project gutenberg docs, and we want to account 
# for possibility of "title: Some Title", "Title: Some Title", and "TITLE: Some Title").
#title_search = re.compile(r'(title:\s*)(?P<title>.*)', re.IGNORECASE)
title_search = re.compile(r'(title:\s*)(?P<title>.*?)(Author:|Illustrator:|Translator:|Release Date:)', re.IGNORECASE|re.DOTALL)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# Now we need to do something with the user supplied keywords
# which we're getting with sys.argv. Remember, the script name itself
# is at index 0 in sys.argv, so we'll slice everything from index 1 forward.
pattern1 = r'(?:.*start of.*?\*\*\*)(?P<subdoc>.*)(?:\*\*\* end of)'
#body_search = re.compile(r'(?:.*start of.*?complete)(.*)(?:end of)', re.IGNORECASE|re.DOTALL)
body_search = re.compile(pattern1, re.IGNORECASE|re.DOTALL)
searches = {}
for kw in sys.argv[1:]:
	pattern = r'\b' + kw + r'\b'
	searches[kw] = re.compile(pattern, re.IGNORECASE)

# now iterate over the documents and extract and print output about metadata
# for each one. Note the use of enumerate here, which gives you a counter variable
# (in this case 'i') that keeps track of the index of the list (in this case documents)
# your currently on in your loop. You should memorize how enumerate works, and google it
# if you need more explanation. It's a highly productive built in function, and there are
# common problems that you'll encounter as a programmer that enumerate is great for.
for i, doc in enumerate(documents):
	#title = re.search(title_search, doc)
	title = re.search(title_search, doc).group('title')
	author = re.search(author_search, doc)
	translator = re.search(translator_search, doc)
	illustrator = re.search(illustrator_search, doc)
	if author: 
		author = author.group('author')
	if translator:
		translator = translator.group('translator')
	if illustrator:
		illustrator = illustrator.group('illustrator')
	print "***" * 25
	#print "Here's the info for doc {}:".format(i)
	print "The title of the text is {}".format(title)
	print "The author(s) is {}".format(author)
	print "The translator(s) is {}".format(translator)
	print "The illustrator(s) is {}".format(illustrator)
	print ""
	print "Here's the counts for the keywords you searched for"
	subdoc = re.search(body_search, doc).group('subdoc')
	for search in searches:
	    print "\"{0}\": {1}".format(search, len(re.findall(searches[search], subdoc)))