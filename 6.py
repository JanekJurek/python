import os
path = r"C:\Users\admin\Desktop\Nowy folder"
a = os.listdir(path)
for i in a:
    os.rename(path + '//' + i, path + '//' + i[:-3] + 'jpg')
