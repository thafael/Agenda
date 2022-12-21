AGENDA = {
    'guilerme': {
        'tel': '96547-8822',
        'email': 'contato@google.com',
        'endereco': 'rua afonso pena 99',
    },
    'maria': {
        'tel': '97878-2588',
        'email': 'maria1000@gmail.com',
        'endereco': 'rua da america 419',
    },
    'joao': {
        'tel': '99929-5192',
        'email': 'joaozinho10@yahoo.com',
        'endereco': '96552-3121'
    },

}
AGENDA['guilerme']['endereco'] = 'rua das nações 24'

AGENDA['lucas'] = {
    'tel': '97280-2011',
    'email': 'lucassilva99@gmail.com',
    'endereco': 'av. carlos maia 25',
}

for contato in AGENDA:
    print(contato)
AGENDA.pop('lucas')

print(AGENDA['lucas'])