import types

def gen(words, punctuation):
    a = list(punctuation)
    iter_words = iter(words)
    
    while True:
        try:
            word = next(iter_words)
        except StopIteration:
            break
        else:
            for next_ in a:
                while len(word) != 0 and next_ == word[0]:
                    word = word[1::]
                while len(word) != 0 and next_ == word[len(word)-1]:
                    word = word[:len(word)-1:]
            if len(word) != 0:
                word = list(word)
                for index, item in enumerate(word):
                    if item == '-':
                        word[index] = ' '
                        
                word = ''.join(word)
                word = word.split(' ')   
                for item in word:
                    yield item
                    
def remove_punctuation(words, punctuation='`~!@#$%^&*()_-+={[}]|\:;"<,>.?/}\t\n'):
    vals = gen(words, punctuation)
    return vals
    
def to_lower(words):
    iter_words = iter(words)
    
    while True:
        try:
            word = next(iter_words)
        except:
            break
        else:
            word = list(word)
            for index, item in enumerate(word):
                word[index] = item.lower()
                
            word = ''.join(word)
            yield word
            
def lower_words(words):
    words = to_lower(words)
    return words

def remove_words(words, stop):
    iter_word = iter(words)
    
    while True:
        try:
            word = next(iter_word)
        except:
            break
        else:
            if stop:
                if type(stop) != list:
                    stop = stop.split(' ')
                    
                if word not in stop:
                    yield word
            else:
                yield word
                
def remove_stop_words(words, stop_words=None):
    vals = remove_words(words, stop_words)
    return vals

def tokenize_line(line, stop_words=None, punctuation='`~!@#$%^&*()_-+={[}]|\:;"<,>.?/}\t\n'):
    rev_punc = remove_punctuation(line.split(' '))
    lower_case = lower_words(list(rev_punc))
    rev_stop = remove_stop_words(list(lower_case), stop_words)
    return rev_stop

def token_lines(lines, stop, punc):
    iter_lines = iter(lines)
    while True:
        try:
            line = next(iter_lines)
        except:
            break
        else:
            tokens = tokenize_line(line, stop, punc)
            for token in tokens:
                yield token
                
def tokenize_lines(lines, stop_words=None, punctuation='`~!@#$%^&*()_-+={[}]|\:;"<,>.?/}\t\n'):
    token = token_lines(lines, stop_words, punctuation)
    return token

def counting_words(words):
    curr_dict = {}
    
    while True:
        try:
            word = next(words)
        except:
            break
        else:
            if word in curr_dict:
                curr_dict[word] += 1
            else:
                curr_dict[word] = 1;
                
    return curr_dict

def count_words(words):
    mydict = counting_words(words)
    return mydict

def sort_dict(dic):
    new_dict = {}
    mydict_vals = sorted(dic.values())
    mydict_items = sorted(dic, key=dic.__getitem__)
    mydict = mydict_vals[::-1]
    mydict_items = mydict_items[::-1]
    
    items = iter(mydict_items)
    vals = iter(mydict)
    
    while True:
        try:
            val = next(vals)
            item = next(items)
        except:
            break
        else:
            yield item, val
            
def sort_word_counts(wc):
    mydict = sort_dict(wc)
    return mydict

def files_to_lines(files):
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                yield line