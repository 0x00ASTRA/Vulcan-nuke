import disk
import encrypt
# import rw
import verify

dl = disk.get_drives()
wipe_list = []

def print_wipe(name,vendor,size,serial):
    print(
        'Wiping Disk: ' + 
        f'{name}'
        + ' | ' + 
        f'{vendor}' 
        + ' | ' + 
        f'Size: {size}' 
        + ' | ' + 
        f'SN: {serial}\n'
    )  

if __name__ == '__main__':
    for drive in dl:
        print_wipe(drive['name'], drive['vendor'], drive['size'], drive['serial'])
        if verify.v_loop():
            encrypt(drive['name'])
            
        elif not verify.v_loop:
            print('Nuke Aborted\n')
        else:
            print('Error: loop value set to null')
    