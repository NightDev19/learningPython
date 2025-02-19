'''
    Extracting The Data
    
    **Given the Collection**
    
    student = [
        [’BSIT’ , [’David’ , ‘Arlene’]],
        [’BSCS’,[’Jaymar’,’Emman’,’Patrick’]]
    ]
    
    Print them in a way that you will Distinguish who are the BSIT and BSCS
    
    NOTE :Only use NESTED FOR LOOP
    
'''

students = [
    ['BSIT', ['David', 'Arlene']],
    ['BSCS', ['Jaymar', 'Emman', 'Patrick']]
]

for student in students:
    print(f'{student[0]} Student')
    for info in student[1]:
        print(f'- {info}')
    print()
