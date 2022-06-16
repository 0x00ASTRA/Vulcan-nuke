#!/usr/bin/python3
import subprocess
import secrets
import multiprocessing
import json
import time
import datetime

class Nuke:
    wipe_list = []

    def get_drives(self):
        cmd = ['lshw', '-c', 'disk', '-json']
        output = subprocess.run(cmd, capture_output=True, text=True)
        with open('drives.json','w') as wf:
            wf.writelines(output.stdout)
            wf.close()

        with open('drives.json') as f:
            disks = json.load(f)

        for disk in disks:
            try:
                disk_name = disk['logicalname']
            except:
                disk_name = 'Unknown'

            try:
                disk_serial = disk['serial']
            except:
                disk_serial = 'Unknown'

            try:
                disk_size = str(int(disk['size']/1000000000)) + 'GB'
            except:
                disk_size = 'Unknown'

            try:
                disk_vendor = disk['vendor']
            except:
                disk_vendor = 'Unknown'

            # if int(disk['size']/1000000000) < 126:
            #     break
            # else:
            self.wipe_list.append(disk_name)
            print(
                'Wiping Disk: ' + 
                f'{disk_name}'
                + ' | ' + 
                f'{disk_vendor}' 
                + ' | ' + 
                f'Size: {disk_size}' 
                + ' | ' + 
                f'SN: {disk_serial}\n'
            )

        inp = input('Would you like to continue?(Y/n): \n')
        proceed = False
        abort = False
        trig = False

        while trig == False:
            if inp.lower() == 'y':
                print('Proceeding to encrption phase...')
                proceed = True
                trig = True

            elif inp.lower() == 'n':
                print('Aborting Nuke...')
                abort = True
                trig = True

            else:
                print('Input not recognized')

        if abort == True:
            print('Nuke aborted')

        if proceed == True:
            self.encrypt()

    def encrypt(self):

        def do_encrypt():
            cmd = [
                'cryptsetup', 'luksFormat', '--type', 'luks1', f'{self.wipe_list[i]}'
            ]
            passwd = secrets.token_bytes(32)

            subprocess.run(cmd, input=passwd)
            print(f'Encrypting volume: {self.wipe_list[i]}\n')        
        for i in range(len(self.wipe_list)): 
            p1 = multiprocessing.Process(target=do_encrypt)
            p1.start()
            
        for _ in range(len(self.wipe_list)):    
            p1.join()
            
        self.shred(self.passes)

    def shred(self, passes):
        def cmd():
            subprocess.run(['shred', '-z', '-v', '-u', '-n', f'{passes}', f'{disk}'])
        procs = []  
        for disk in self.wipe_list:
            print('Process started for: ' +  f'{disk}')
            p1 = multiprocessing.Process(target=cmd)
            procs.append(p1)
            p1.start()

        time.sleep(2)
        
        print(procs)
        for proc in procs:
            proc.join(timeout=0)
            while proc.is_alive() != None:
                time.sleep(0)
            print('completed ' + self.wipe_list[proc] + "@" + datetime.datetime())
        self.check_drive()
    

    def check_drive(self):
        command = ['badblocks','-sv', '-t', '0x00', f'{self.wipe_list[i]}']
        for i in self.wipe_list:
            subprocess.run(command)

    def __init__(self):
        self.passes = input('How many passes would you like to make? \n')
        self.get_drives()

if __name__ == '__main__':
    print('==============================================================================================')
    print('** Warning: This Program will cause irreversable destruction to the data of disks attached. **')
    print('==============================================================================================')
    print('')
    Nuke()