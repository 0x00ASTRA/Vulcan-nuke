# read and write data to a disk
data = []
blockcount = 0
bc2 = 0
bc3 = 0


with open('/dev/sdb', 'rb') as f, open('/dev/sdb', 'wb') as w:
    while blockcount < 5:
        block = f.read(1)
        blockcount +=1
        print('Blockcount: ' + str(blockcount))
        print('byte: ' + str(block))

    while bc2 < 5:
        block = w.write(b'\0')
        bc2 += 1

print('')
print("Block Count: " + str(blockcount))

# with open('readfile.text', 'w') as l:
    # l.writelines(data)
