from art import logo, vs
from game_data import data
from replit import clear
from random import randint
from time import sleep

score = 0

def gera_usuario():
  usuario = data[randint(0, (len(data)-1))]
  return usuario

  
def calculate_followers(user1, user2):
  if user1['follower_count'] > user2['follower_count']:
    most_follows = user1
  else:
    most_follows = user2
  return most_follows


def solicita_palpite():
  while True:
    guess = input("\nQuem tem mais seguidores? A ou B?: ").strip().upper()
    
    if guess == "A":
      guess=usuario1
    elif guess == "B":
      guess=usuario2
    else:
      print("Resposta inválida")
      continue
    return guess

def analisa_palpite(palpite, most_followers):
  global score
  if palpite == most_followers:
    print(f"""Você acertou!!!
            \n{usuario1["name"]}: {usuario1["follower_count"]}
            \n{usuario2["name"]}: {usuario2["follower_count"]}
            """)
    score += 1
    return False
  else:
    print(f"""Você errou! FIM DE JOGO
          \n{usuario1["name"]}: {usuario1["follower_count"]}
          \n{usuario2["name"]}: {usuario2["follower_count"]}
          """)
    return True
    
def sequencia_prints(usuario1, usuario2):
  # printar logo
  print(logo)
  
  # printar pontuação
  print(f"score: {score}")

   # printar usuário 1
  print(f"Compare A: {usuario1['name']}, {usuario1['description']} from {usuario1['country']}")

   # VS
  print(vs)

  # printar usuario 2
  print(f"Com B: {usuario2['name']}, {usuario2['description']} from {usuario2['country']}")
  
# Receber usuarios aleatorio


usuario1 = gera_usuario()
usuario2 = gera_usuario()

while True:
  sequencia_prints(usuario1, usuario2)
  # calcular quem tem o maior numero de seguidores
  most_followers = calculate_followers(usuario1, usuario2)
  
  palpite = solicita_palpite()
  
  game_over = analisa_palpite(palpite, most_followers)
  if game_over == True:
    break

  sleep(3)

  usuario1 = most_followers
  usuario2 = gera_usuario()
  
  clear()