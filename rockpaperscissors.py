import random
def optionn():
	global option 
	option = input("Insira uma opção: ")
optionn()
all = ["pedra", "papel", "tesoura"]
computer_action = random.choice(all)
#print com f formata para string todos os dados que estão concatenados
print(f"\nVocê escolheu {option}, computador escolheu {computer_action}")
#situação 01
if option == "pedra":
	if computer_action == "tesoura":
		print("\nVocê ganhou! Pedra esmaga tesoura")
	if computer_action == "pedra":
		print("\nEmpate! Escolha outra opção")
		optionn()
	if computer_action == "papel":
		print("\nVocê perdeu! Papel embala pedra")
#situação 02
if option == "papel":
	if computer_action == "tesoura":
		print("\nVocê perdeu! Tesoura corta papel")
	if computer_action == "papel":
		print("\nEmpate! Escolha outra opção")
		optionn()
	if computer_action == "pedra":
		print("\nVocê ganhou! Papel embala pedra")
#situação 03
if option == "tesoura":
	if computer_action == "papel":
		print("\nVocê ganhou! Tesoura corta papel")
	if computer_action == "tesoura":
		print("\nEmpate! Escolha outra opção")
		optionn()
	if computer_action == "pedra":
		print("\nVocê perdeu! Pedra amassa tesoura")
