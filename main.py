
import disk
import encrypt
import rw
import time
import multiprocessing as mp

dl = disk.get_drives()
wipe_list = []
size_list = []
vendor_list = []

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
    response = input('Would you like to wipe this drive?(y/n): ')

    return response.lower() == 'y'

def main():
    cont = False
    for drive in dl:
        pw = print_wipe(drive['name'], drive['vendor'], drive['size_gb'], drive['serial'])
        dr, ven, size_gb, size_b =  drive['name'], drive['vendor'], drive['size_gb'], drive['size_bytes']
        
        if pw == True:
            print('')
            print(f'encrypting {dr}')
            print('')

            wipe_list.append(dr)
            size_list.append(size_b)
            vendor_list.append(ven)
        else:
            print('')
            print(f'Skipping wipe for {dr}')
            print('')

    print('Confirming Wipe: ')
    for wl in wipe_list:
        print(wl)
        print('')
    
    conf = input("Are you sure you would like to continue? ('YES'/N): ")
    if conf.upper() == 'YES':
        print('')
        print('Continuing...')
        print('')
        cont = True

    else:
        print('')
        print('Exiting...')
        print('')
    
    return cont



if __name__ == '__main__':
    if main() == True:
        for wl, sl in zip(wipe_list, size_list):
            encrypt.encrypt_drive(wl)
            do_rw = rw.ReadWrite(wl, int(sl))
            rproc = mp.Process(target=do_rw.read_bytes)
            wproc = mp.Process(target=do_rw.write_bytes)
            wproc.start()
            wproc.join()
            time.sleep(2)
            rproc.start()
            rproc.join()
