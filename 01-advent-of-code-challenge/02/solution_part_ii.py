mapa = {'A': 'Pedra', 'B': 'Papel', 'C': 'Tesoura', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
pontos = {'Pedra': 1, 'Papel': 2, 'Tesoura': 3}
pontoo = {'Lose': 0, 'Draw': 3, 'Win': 6}

def points_per_round2(round_string):
    ladoo = mapa[round_string[0]]
    our_goal = mapa[round_string[2]]

    if (ladoo, our_goal) in [('Pedra', 'Draw'), ('Papel', 'Lose'), ('Tesoura', 'Win')]:
        return pontoo[our_goal] + pontos['Pedra']
    elif (ladoo, our_goal) in [('Pedra', 'Win'), ('Papel', 'Draw'), ('Tesoura', 'Lose')]:
        return pontoo[our_goal] + pontos['Papel']
    else:
        return pontoo[our_goal] + pontos['Tesoura']
    
sum([points_per_round2(round_string) for round_string in rounds])
