#todolist
s=''
f=dict()

s=input('Ввод новой задачи, просмотр списка задач, или выход: ')
while s!='Выход':
    if s=='Список':
        print(f)
    else:
        f[s]={}
        f[s]['Категория']=input('Введите категорию задачи или заметку об её отсутствии: ')
        f[s]['Срок']=input('Введите срок выполнения задачи или отметку об его отсутствии: ')
    s=input('Ввод новой задачи, просмотр списка задач, или выход: ')
        
    
