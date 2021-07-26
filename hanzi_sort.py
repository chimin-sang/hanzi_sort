from pathlib import Path

data_path = Path(__file__).resolve().with_name('dictionary.txt')
lines = data_path.read_text(encoding='utf-8').splitlines()

pinyin_index = {}
bihua_index = {}

for line in lines:
    key, pinyin, bihua = line.split()
    bihua_index[key] = bihua
    pinyin_index[key] = pinyin

def lpad14(c):
    return "{0:x}".format(ord(c)).zfill(14)
            
def pinyin_order(s):
    return ''.join([pinyin_index.get(x, lpad14(x)) for x in s])        
    
def bihua_order(s):
    return ''.join([bihua_index.get(x, lpad14(x)) for x in s])

