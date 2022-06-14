import json
import subprocess

class Disk:
    def __init__(self, logicalname, vendor, size, serial):
        self.logicalname = logicalname
        self.vendor = vendor
        self.size = size
        self.serial = serial
    
    def print_wipe(self):
        print(
            'Wiping Disk: ' + 
            f'{self.logicalname}'
            + ' | ' + 
            f'{self.vendor}' 
            + ' | ' + 
            f'Size: {self.size}' 
            + ' | ' + 
            f'SN: {self.serial}\n'
        )       

# get attached drives
def get_drives():
    wipe_list = []
    disk_list = []
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
            disk_size_gb = str(int(disk['size']/1000000000)) + 'GB'
        except:
            disk_size_gb = 'Unknown'
        
        try:
            disk_size_bytes = (disk['size'])
        except:
            disk_size_bytes = 'Unknown'


        try:
            disk_vendor = disk['vendor']
        except:
            disk_vendor = 'Unknown'
        
        if not disk_name in wipe_list:
            wipe_list.append(disk_name)
            # d = Disk(disk_name, disk_vendor, disk_size, disk_serial)
            # d.print_wipe()
            disk_dict = {'name': disk_name, 'vendor': disk_vendor, 'size_bytes' : disk_size_bytes, 'size_gb' : disk_size_gb, 'serial' : disk_serial}
            disk_list.append(disk_dict)
            

    return disk_list
