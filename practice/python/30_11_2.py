#ass2:write a program to identify the file format
s=input()
if s.endswith('jpeg'):
    print('Photo document')
elif s.endswith('doc'):
    print('Word document')
elif s.endswith('xls'):
    print('Excel document')
elif s.endswith('ppt'):
    print('Powerpoint document')
else:
    print('Invalid document')