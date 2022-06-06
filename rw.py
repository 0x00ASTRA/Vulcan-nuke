# read and write data to a disk
import datetime
from itertools import count

class ReadWrite:
    def __init__(self, path, size, write_zeros):
        self.path = path
        self.size = size
        self.write_zeros = write_zeros
        self.start_time = datetime.datetime.now()
        self.itr = count()

    def read_bytes(self, filepath, bytes):
        with open(f'{self.path}', 'rb') as f:
            try:
                block = f.read(512)
            except:
                block = 'Error Reading Block'
        return block

    def write_bytes(self, filespath, bytes):
        with open(f'{self.path}', 'wb') as w:
            try:
                wr_block = w.write(b'\0')
            except:
                wr_block = 'Error Writing Block'
        return wr_block
    
    def process_completed_at(self):
        self.end_time = datetime.datetime.now()

        return self.end_time


# with open('/dev/sda', 'rb') as f, open('/dev/sda', 'wb') as w:
#     for _ in range(0, maxbytes):
#         wr = w.write(b'\0')
#         block = f.read(1)
#         blockcount +=1
#         etc = (blockcount / time.time()) / (maxbytes - blockcount)
#         print('Blockcount: ' + str(blockcount) + ' byte: ' + str(block) + ' etc: ' + str(etc), end='\r')
#         print('')
        

# end_time = datetime.datetime.now()
# print('')
# print('Start Time: ' + str(start_time) + ' | ' + 'End Time: ' + str(end_time) + ' | ' + 'Exec Time: ' + str(end_time - start_time))

# with open('readfile.text', 'w') as l:
    # l.writelines(data)
