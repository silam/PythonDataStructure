

"""
https://www.youtube.com/watch?v=X41iojWqQZY&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=3
"""


from Stack import Stack

def div_by_two(dec_num):
    s = Stack()
    
    while dec_num > 0 :
        r = dec_num % 2
        s.push(r)

        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

print (div_by_two(242))


