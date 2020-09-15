import re
phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}') # compiles the raw string marked by r
mo = phoneNum.search('My number is 444-233-1234')
print ('Phone number found is: {} '.format(mo.group())) # .group() displays the whole match found
                        # without .group() output is Phone number found is: <re.Match object; span=(13, 25), match='444-233-1234'


phoneNumregex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # splits the raw string to form two groups
mo = phoneNumregex.search('My number is 444-233-1234')
areaCode, mainNumber = mo.groups() # .groups() identifies the split

phone = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})') #\( \) will match actual paranthesis characters
mo = phone.search('My number is (444) 233-1234')
areaCode, mainNumber = mo.groups()

print(areaCode)
print(mainNumber)

# matching groups with a pipe. Will match either Tina fey or maria or sizzla
heroRegex = re.compile (r'Tina (Fey|Maria|sizzla)')
mo1 = heroRegex.search('Batman, Tina Fey, Riri and Lexus .')
print(mo1.group())
mo2 = heroRegex.search('Batman, Tina sizzla, Riri and Lexus .') 
print (mo2.group())

#? flags the group that precedes it as an optional part of the pattern
batRegex = re.compile(r'Bat(wo)?man')
mo3 = batRegex.search('The Adventures of Batman')
print (mo3.group())
mo4 = batRegex.search('The Adventures of Batwoman')
print (mo4.group())

# * matches the preceding group with ZERO or MORE eg. in above example 
# bat(wo)*man can search: batman result batman, batwowowowoman result to 
# batwowowowoman

# + matches the preceding group with ONE or MORE eg. in above example 
# bat(wo)+man can search: batman result to None value,batwoman result to 
# batwoman, batwowowowoman result to batwowowowoman

# matching repetitions. re.compile(r'Ha{3}') will match for HaHaHa but Ha
# returns None. Ha{3,5} will match as (Ha){3,} will
# match three or more instances of the (Ha) group, while (Ha){,5} will match
# zero to five instances

# Greedy regular expressions are default in python as in will match for longest
# string possible while nongreedy will match for shortest string possible

greedyRegex = re.compile(r'(Ha){3,5}')
mo5 = greedyRegex.search('HaHaHaHa, HaHaHa')
print(mo5.group())

nongreedyRegex = re.compile(r'(Ha){3,5}?') # }?, *?, +? declares a nongreedy match
mo6 = nongreedyRegex.search('HaHaHaHa, HaHaHa')
print(mo6.group())

# .findall() works as .search() but will return any match(es) found as list if there
# are no groups 

phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
mo = phoneNum.findall('My home number is 444-233-1234 and work number is 455-324-7456')
print ('Phone number found is: {} '.format(mo))

phoneNum = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups
mo = phoneNum.findall('My home number is 444-233-1234 and work number is 455-324-7456')
print ('Phone number found is: {} '.format(mo))

# Find more of regex usage in python in regex2.py. 
# Probably attached in the same folder. 