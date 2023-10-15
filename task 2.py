import os

def file_read():
    data = {}
    for i in range(1,4):
        with open(f'{i}.txt','r', encoding='utf-8') as f:
            text = f.readlines()
            data[f'Файл {i}.txt'] = [len(text),text]
    return data
'''как выглядит плохой код'''
# def file_write(data):
#     f = open('result.txt','w',encoding='utf-8')
#     data_sorted = []
#     for k,v in data.items():
#         data_sorted.append([v[0],k])
#     data_sorted.sort()
#     for i in data_sorted:
#         f.write(f'{i[1]}\n{i[0]}\n')
#         for j in data[i[1]][1]:
#             f.write(j)
#         f.write('\n')

'''как должен выглядить хороший код'''
def compile_files(path):
    data = {}
    for file_ in path:
      if file_.endswith('.txt'):
        with open(file_, encoding="utf-8") as f:
            file_data = f.readlines()
            #print(file_data)
            data[len(file_data)] = (file_, " ".join(file_data))

    data = dict(sorted(data.items()))

    with open("result_data.txt", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            print(key, value)
            new_file.write(f"{value[0]} \n")
            new_file.write(f"{key} \n")
            new_file.write(f"{value[1]}\n\n")




file = file_read()
compile_files(os.listdir) #
