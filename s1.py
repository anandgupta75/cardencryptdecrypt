import sys
def f1(j3):
    ed1='DecryptEncrypted'
    s1=''
    count=0
    for i in j3:
        s1=s1+chr(ord(i) ^ ord(ed1[count]))
        count+=1
        if count==16:
            break
    print(line.strip()+" "+s1)

with open(sys.argv[1])as f4:
    for line in f4:
        f1(line)
