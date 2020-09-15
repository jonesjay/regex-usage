# character classes
# \d   Any numeric digit from 0 to 9.
# \D   Any character that is not a numeric digit from 0 to 9.
# \w   Any letter, numeric digit, or the underscore character.
# \W   Any character that is not a letter, numeric digit, or the
#      underscore character.
# \s   Any space, tab, or newline character. (Think of this as
#      matching “space” characters.)
# \S   Any character that is not a space, tab, or newline.
# eg. code 
#            song=re.compile(r'\d+\s\w+')
#            song.findall('5 golden , 2 dozen ')
# will match anything that starts with digit then space then a word.
# 

import re
vowel = re.compile(r'[a-gA-G0-9?/]') #making own character class with square brackets 
res = vowel.findall('hUngry1 fox jumps Over Lazy-dOg?')
print (res)

vowelNot = re.compile(r'[^aeiouAEIOU]') #negates the character class
resnot = vowelNot.findall('hUngry fox jumps Over Lazy dOg.')
print (resnot)

ends = re.compile(r'^\w+') # searches the first word 
ends = ends.findall('Hello there, this is your captain speaking')
print (ends)

firsts = re.compile(r'\d+$')
firsts = firsts.search('This car costs Ksh.45000')
print (firsts.group())

# . (dot) character is a wildcard and matches any character except for newline
at = re.compile(r'.at')
at = at.findall('Cat has flat pat.')# dot will only match one preceding character 
fore = re.compile(r'\.')
fore = fore.findall('Cat has flat pat.')
print (at)
print (fore)

# to match everthing .*
name = re.compile(r'First Name: (.*) Last Name: (.*)')
name = name.search('First Name: John Last Name: Doe')
print (name.groups())
#print (name.group(2))

# dot uses greedy mode always unless ...
nongreedy = re.compile(r'First Name: (.*?) Last Name: (.*?)')
nongreedy = nongreedy.search('First Name: John Last Name: Doe')
print (nongreedy.group())

#dot excludes matching newline unless by passing re.DOTALL
noNewline = re.compile('.*')
print (noNewline.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newline = re.compile('.*', re.DOTALL)
print (newline.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# To ignore case sensitive words passing re.IGNORECASE or re.I as second argument 
# to re.compile

station = re.compile(r'Ksh \d*')
station = station.sub('**censored**', 'The total amount received by the organisation was Ksh 500000 proving their guilt')
print (station)

# or 
station1 = re.compile(r'Ksh (\d)\d*')
station1 = station.sub(r'\1****', 'The total amount received by the organisation was Ksh 500000 proving their guilt')
print (station1)

phoneRegex = re.compile(r'''(  # uses triple comma to allow multiple lines
(\d{3}|\(\d{3}\))?            # area code
(\s|-|\.)?                    # separator  
\d{3}                         # first three digits  
(\s|-|\.)                     # separator    
\d{4}                         # last four digits
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension  
)''', re.VERBOSE)

# re.compile function takes only one more argument as second argument, to 
# join various argument pipe(also bitwise or operator ) is used
# like: newline = re.compile('.*', re.DOTALL | re.I | re.verbose)
