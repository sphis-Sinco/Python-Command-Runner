version = 'pv1' # prototype version 1

commands = [
        {
                'name': 'Change drive',
                'command': '$1:'
        }
]

print(f'Welcome to Command Runner v.${version}')

while True:
        cmd = input('What command would you like to enter?\n> ')

        i = 0
        while i < commands.__len__():
                if commands[i].get('name').lower() == cmd.lower():
                        print(f'Command found! (${i}/${commands.__len__()})')

                i = i + 1
        print('Command not found')