"""
GENERATE NEWSLETTER.
"""
from nsbelmu import NSBEAI

model = NSBEAI()
meeting = input('[ :| ] Enter the type of the next chapter meeting: ').capitalize()
print(f'[ :) ] {meeting}')
date = input('[ :| ] Enter the date of the next chapter meeting: ').capitalize()
print(f'[ :) ] {date}')
print('[ :| ] Generating newsletter...')
output = model.generate_newsletter(meeting, date)
print('[ :) ] Newsletter generated!')
print(output)
