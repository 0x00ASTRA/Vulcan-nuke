#!/usr/bin/bash python3
import subprocess
import secrets
import multiprocessing
import json


class Shred:
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
            disk_name = disk['logicalname']
            disk_serial = disk['serial']
            disk_size = str(int(disk['size']/1000000000)) + 'GB'
            disk_vendor = disk['vendor']
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
            if inp == 'y':
                print('Proceeding to encrption phase...')
                proceed = True
                trig = True
            
            elif inp == 'Y':
                print('Proceeding to encrption phase...')
                proceed = True
                trig = True

            elif inp == 'n':
                print('Aborting Nuke...')
                abort = True
                trig = True
            
            elif inp == 'N':
                print('Aborting Nuke...')
                abort = True
                trig = True

            else:
                print('Input not recognized')
        
        if abort == True:
            Print('Nuke aborted')
        
        if proceed == True:
            self.encrypt()
        
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
        
        self.shred(self.passes)

    def shred(self, passes):
        for i in range(len(self.wipe_list)):

            def do_shred():
                disk = self.wipe_list[i]
                proc = subprocess.run(['shred', '-z', '-v', '-u', '-n', f'{passes}', f'{disk}'])
                # with open(f'{disk}-shredlog.txt', 'w') as f:
                #     f.writelines(proc.stdout)
                return proc

            p1 = multiprocessing.Process(target=do_shred)
            p1.start()
            
        for _ in range(len(self.wipe_list)):
            p1.join()
    
    def __init__(self):
        self.passes = input('How many passes would you like to make? \n')
        self.get_drives()

if __name__ == '__main__':
    Shred()
