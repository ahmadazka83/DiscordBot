from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered.startswith('~'):
        if lowered == '':
            return 'Ngomong apa bang...'
        elif '~halo' in lowered:
            return 'Halo bang!'
        elif '~gacha' in lowered:
            rolls = randint(1, 100000)
            if rolls >= 99998:
                return f'Selamat anda dapat 10000$. Rolls anda: {rolls}'
            elif rolls >= 99900:
                return f'Selamat anda dapat 1000$. Rolls anda: {rolls}'
            elif rolls >= 99000:
                return f'Selamat anda dapat 100$. Rolls anda: {rolls}'
            elif rolls >= 90000:
                return f'Selamat anda dapat 10$. Rolls anda: {rolls}'
            else:
                return f'Selamat anda dapat 1$. Rolls anda: {rolls}'
        elif '~presiden' in lowered:
            return choice(['Anies','Prabowo','Ganjar'])
        else:
            return choice(['Gak ngerti','Maksudnya?','Hah??'])