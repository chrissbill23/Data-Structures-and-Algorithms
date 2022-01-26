
# Trie (prefix tree) data structure with all operations in O(n) where n is the length of the string

class TrieChar:
    def __init__(self, char=None):
        self.char = char
        self.isWord = False
        self.pos = 0
        self.children = {}
        
class Trie:
    
    def __init__(self):
        self.__root = TrieChar()
        self.__dictionary = set()
        
    def __getNode(self, word)->TrieChar:
        curr_node = self.__root
        for char in word:
            charLower = char.lower()
            if charLower in curr_node.children:
                curr_node = curr_node.children[charLower]
            else:
                break
        return curr_node
        
    def insert(self,word: str):
        curr_node = self.__root
        i = 0
        while i < len(word):
            charLower = word[i].lower()
            if charLower not in curr_node.children:
                curr_node.children[charLower] = TrieChar(charLower)
                curr_node.children[charLower].pos = i+1
                if i == len(word)-1:
                    curr_node.children[charLower].isWord = True
            curr_node = curr_node.children[charLower]
            i+=1
        self.__dictionary.add(word)
        
    def search(self,word:str)->bool:
        return self. __getNode( word).isWord
    
    def startsWith(self, pref: str)->bool:
        return self. __getNode(pref).pos == len(pref)
        
    def __str__(self):
        s = ''
        queue = [self.__root]
        while len(queue) > 0:
            node = queue.pop(0)
            s+=(node.char or '*')+'-->('
            for child in node.children:
                s+=node.children[child].char+','
                queue.append(node.children[child])
            s+=')\n'
        return s
    
    def __repr__(self):
        return self.__str__()
        
    
    

        
        