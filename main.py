
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
    response = input('Would you like to wipe this drive?(y/n): ')

    return response.lower() == 'y'

def main():
    for drive in dl:
        pw = print_wipe(drive['name'], drive['vendor'], drive['size_gb'], drive['serial'])
        dr, ven, size =  drive['name'], drive['vendor'], drive['size_gb']
        
        if pw == True:
            print('')
            print(f'encrypting {dr}')
            print('')

            wipe_list.append(dr)
        else:
            print('')
            print(f'Skipping wipe for {dr}')
            print('')

    print('Confirming Wipe: ')
    for wl in wipe_list:
        print(wl)
        print('')
    
    conf = input('Are you sure you would like to continue? (YES/NO): ')
    if conf.upper() == 'YES':
        print('')
        print('Continuing...')
        print('')
    else:
        print('')
        print('Exiting...')
        print('')



if __name__ == '__main__':
    main()
