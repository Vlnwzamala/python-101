num_eps = int(input('How many employee records do you want to create? '))

with open ('employess.txt','w') as emp_file:
    for count in range(1, num_eps + 1):
        print('Enter data for Employee#', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()

print('Employee recrds written to employees.txt.SSS')