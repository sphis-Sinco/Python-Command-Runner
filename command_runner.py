import subprocess


version = 'pv2' # prototype version 2

commands = [
        {
                'name': 'Change drive',
                'command': '$1:'
        }
]

print(f'Welcome to Command Runner v.{version}')

while True:
        cmd = input('What command would you like to enter?\n> ')

        i = 0
        found_command = False
        command = ''

        while i < commands.__len__():
                if commands[i].get('name').lower() == cmd.lower():
                        print(f'Command found! ({i + 1}/{commands.__len__()})')
                        command = cmd.lower()
                        found_command = True

                i = i + 1

        if not found_command:
                print('Command not found')

        if found_command:
                if command == 'change drive':
                        drive = input('What drive would you like to switch to?\n> ')
                        subprocess.run(f'{drive}:')