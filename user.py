#!/usr/bin/env python3.6

users = [
        {'admin':True, 'active': True, 'name':'Yesh'},
        {'admin':False, 'active': True, 'name':'Ved'},
        {'admin':False, 'active': False, 'name':'Deepthi'},
        ]

line=1
for user in users:
    prefix=f"{line}"

    if user['admin'] and user['active']:
        prefix+="ACTIVE-(ADMIN)"
    elif user['admin']:
        prefix+="(ADMIN)"
    elif user['active']:
        prefix+="ACTIVE-"
    print(prefix+ user['name'])
    line+=1
