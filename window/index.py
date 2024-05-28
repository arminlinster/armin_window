with open('names.txt', encoding='utf-8') as file1:
    content:str = file1.read()
    '''
    print("----")
    print(file1.read())
    #print(content)
    '''
    names:list[str] = content.split()
    len(names)
    print(len(names))
    pass
print(file1.closed)