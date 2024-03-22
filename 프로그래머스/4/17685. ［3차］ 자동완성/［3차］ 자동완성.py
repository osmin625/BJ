def solution(words):
    def make_trie(words):
        root = {}
        for word in words:
            current = root
            for letter in word:
                if letter not in current:
                    current[letter] = {'cnt_':0}
                current = current[letter]
                current['cnt_'] += 1
            current['*'] = True
        return root
    
    def search_(trie, word):
        current = trie
        lvl = 0
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
            lvl += 1
            if current['cnt_'] == 1:
                return lvl
        if '*' in current:
            return lvl
            
    
    trie = make_trie(words)
    answer = []
    for word in words:
        answer.append(search_(trie, word))
    return sum(answer)
        
'''
{'g': {
    'o': {
        '*': True, 
        'n': {
            'e': {
                '*': True
                }
            }
        }, 
    'u': {
        'i': {
            'l': {
                'd': {
                    '*': True
                    }
                }
            }
        }
    }
}
'''
