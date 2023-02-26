mapa = {'A': 'Pedra', 'B': 'Papel', 'C': 'Tesoura', 'X': 'Pedra', 'Y': 'Papel', 'Z': 'Tesoura'}
pontos = {'Pedra': 1, 'Papel': 2, 'Tesoura': 3}
pontoo = {'Lose': 0, 'Draw': 3, 'Win': 6}

with open('input2.txt', 'r') as f:
    lines = f.readlines()
    rounds = [entry.strip() for entry in lines]

def points_per_round(round_string):
  ladoo = mapa[round_string[0]]
  ladoseu = mapa[round_string[2]]

  if ladoo == ladoseu:
     return pontoo['Draw'] + pontos[ladoseu]
  elif (ladoo, ladoseu) in [('Papel', 'Pedra'), ('Pedra', 'Tesoura'), ('Tesoura', 'Papel')]:
      return pontoo['Lose'] + pontos[ladoseu]
  else:
      return pontoo['Win'] + pontos[ladoseu]


sum([points_per_round(round_string) for round_string in rounds])
