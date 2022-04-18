import subprocess
import secrets
import multiprocessing

class Shred:
    drive_list = ['/dev/sda', '/dev/sdb', '/dev/sdc', '/dev/sdd', '/dev/sde', '/dev/sdf', '/dev/sdg']
    wipe_list = drive_list[+1:7]

    def get_drives(self, index):
        cmd = 'sudo lshw -class disk -short'
        drive_list = ['/dev/sdb'] #change to output of cmd
        print(drive_list[0])
        return drive_list[index]

    def encrypt(self):

        for i in range(len(self.wipe_list)):

            def do_thing():

                cmd = [
                    'cryptsetup', 'luksFormat', '--type', 'luks1', f'{self.wipe_list[i]}'
                ]
                passwd = secrets.token_bytes(32)         

                subprocess.run(cmd, input=passwd)
                print(f'Encrypting volume: {self.wipe_list[i]}\n')

            p1 = multiprocessing.Process(target=do_thing)
            p1.start()
    
        for _ in range(len(self.wipe_list)):
            p1.join()

    def shred(self, passes):
        for i in range(len(self.wipe_list)):

            def do_shred():
                subprocess.run(['shred', '-v', '-n', f'{passes}', self.wipe_list[i]])

            p1 = multiprocessing.Process(target=do_shred)
            p1.start()
            
        for _ in range(len(self.wipe_list)):
            p1.join()
    
    def __init__(self):
        self.passes = input('How many passes would you like to make? ')
        self.encrypt()
        self.shred(self.passes)

if __name__ == 'main':
    Shred()
