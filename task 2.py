

def file_read():
    data = {}
    for i in range(1,4):
        with open(f'{i}.txt','r', encoding='utf-8') as f:
            text = f.readlines()
            data[f'Файл {i}.txt'] = [len(text),text]
    return data

def file_write(data):
    f = open('result.txt','w',encoding='utf-8')
    data_sorted = []
    for k,v in data.items():
        data_sorted.append([v[0],k])
    data_sorted.sort()
    for i in data_sorted:
        f.write(f'{i[1]}\n{i[0]}\n')
        for j in data[i[1]][1]:
            f.write(j)
        f.write('\n')


file = file_read()
file_write(file)


#file_read()