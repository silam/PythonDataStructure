
"""
https://www.youtube.com/watch?v=X41iojWqQZY&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=3
"""

from Stack import Stack


def  is_match(p1,p2):
    if p1 == "[" and p2 == "]": 
        return True
    elif p1 == "{" and p2 =="}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    else:
        return False

def is_parem_balanced(paran_string):
    s = Stack()
    
    is_balanced = True
    index = 0
    
    
    
    while index < len(paran_string) and is_balanced:

        paren = paran_string[index]

        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                print ("here 1")
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    print ("here 2")
                    is_balanced = False
        index = index + 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print (is_parem_balanced("[({})]"))

