import pickle as pickle

d = dict(url='index.html', title='title', contetn='content')
pickle.dumps(d)
print(d)

f = open(r'.\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open(r'.\dump.txt', 'rb')
loader = pickle.load(f)
f.close()
print(loader)