import secrets
import subprocess
import multiprocessing

def encrypt_drive(drive_path):

    cmd = [
        'cryptsetup', 'luksFormat', '--type', 'luks1', f'{drive_path}'
    ]
    passwd = secrets.token_bytes(32)

    en = subprocess.run(cmd, input=passwd)
    print(f'Encrypting volume: {drive_path}\n')

    p1 = multiprocessing.Process(target=en)
    p1.start()
               
    p1.join()
    