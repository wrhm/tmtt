# langLearner.py
# William Howard Matchen
# Date Created: 18 May 2016
#  Last Edited: 08 Jul 2016

'''
Idea:
	- Inspired by LearnerBot (which queries every word entered until a consistent vocabulary is reached)
	- Zero-knowledge (ground-up) foreign language learner/translator
	- Asks about new vocab
	- Human user should be able to translate text between any two recognized languages
	- How to account for different writing systems and special characters?

>> Select languages (to from, e.g. "en es"): 

Check dictionary for entire text, then for phrases, then words

'''

abbrs = {'English':'en','Spanish':'es','Malay':'ma'}
print abbrs.itervalues()
print 'Available languages: '+', '.join(['%s (%s)'%(x,abbrs[x]) for x in abbrs])
languages = raw_input('Select languages (to from, e.g. "en es"): ')
langIDs = languages.split()
if len(langIDs) != 2:
	print 'Must select two language IDs. Exiting...'
	exit()
all_abbrs = [abbrs[x] for x in abbrs]
for e in langIDs:
	# if e not in abbrs.itervalues():
	if e not in all_abbrs:
		print 'Invalid language ID: \"%s\". Exiting...'%e
		exit()
[fromAbbr,toAbbr] = langIDs
[fromLang] = [x for x in abbrs if abbrs[x]==fromAbbr]
[toLang] = [x for x in abbrs if abbrs[x]==toAbbr]
# fromAbbr,toAbbr = abbrs[fromLang],abbrs[toLang]
raw_input('Translate (%s --> %s): '%(fromAbbr,toAbbr))
