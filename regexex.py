import re

txt = '''
123-123-1234
704.234.5677
800-123-45786
800-788-7896
900-785-7859
990-852-8745    
655-758-7896
'''
#when match with range
pattern = re.compile(r'[6-8]\d\d.\d\d\d.\d\d\d\d')
#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.findall(txt)
print(matches)
