'''
with open('names.txt', encoding='utf-8') as file1:
    content:str = file1.read()
    
    names:list[str]  = content.split()
    len(names)
    print(len(names))
    pass
print(file1.closed)
'''
def get_names() -> list[str]:
    with open('names.txt', encoding='utf-8') as file1:
        content:str = file1.read()
    names:list[str]  = content.split()
    return names    

names:list[str] = get_names()
print(names)
print(len(names))