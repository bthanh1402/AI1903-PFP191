#Q3.1
dict1 = {'Ten':10, 'Twenty':20, 'Thirty':30}
dict2 = {'Thirty':30, 'Fourty':40,'Fifty':50}
for i in dict2.keys():
    dict1[i] = dict2[i]
print(dict1)

#Q3.2
sampleDict = {
    "class": {
        'student':{
            'name':'Mike',
            'marks': {
                'physics':70,
                'history':80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

#Q3.3
employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'salary':8000}

dict3 = {employees[0]: defaults, employees[1]:defaults}
print(dict3)