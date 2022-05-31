def verify_nuke(inp):
    out_str = 'null'
    if inp.lower() == 'y':
        out_str = 'proceed'

    elif inp.lower() == 'n':
        out_str = 'abort'
    
    else:
        print('Input not recognized\n')
    
    return out_str

def v_loop():
    outp = 'Null'
    while True:
        if verify_nuke(input('Would you like to continue?(Y/n): ')) == 'proceed':
            print('')
            print('Proceeding to encrption phase...\n')
            outp = True
            break
        
        elif verify_nuke(input('Would you like to continue?(Y/n): ')) == 'abort':
            print('')
            print('Aborting Nuke...\n')
            outp = False
            break
    
    return outp

