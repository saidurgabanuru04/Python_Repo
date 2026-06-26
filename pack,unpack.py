#packing 
print("              packing                       ")
def pack(*names):
    for i in (names):
        print(f'packing:{i}')
    print(f'packed:{names}')
pack('seeta','rama','krishna','radha')

#unpacking 
print("             unpacking                      ")
def unpack(a,b,c,d):
    print(f'unpacked:a,b,c,d={a},{b},{c},{d}')
name=(1,2,3,4)
unpack(*name)

#packing Dictionary
print("             packing Dictionary             ")
def packdict(**students):
    for i in (students):
        print(f"pack:{i}= {students[i]}")
packdict(std1 = 'a', std2 ='b', std3 ='c')

#unpacking Dictionary
print("             unpacking Dictionary            ")
def unpackdict(a,b,c):
    print(f'''unpacked:
          a={a}
          b={b}
          c={c}''')
d= dict( a=1,b=2,c=3)
unpackdict(**d)