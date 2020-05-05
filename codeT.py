#coding:utf-8
playgame = True
print("please, choice your id and your password")

identifiant = input("id : ")
import getpass
mdp = getpass.getpass("password : ")
	

print("connection interface")

u_id = input("enter your id : ")
u_mdp = input("Enter your password : ")


if u_id == identifiant and  u_mdp == mdp:
	print("you are connected, welcome, ", u_id)
	while playgame:
		menuchoice = input("> ")

		if menuchoice == "again":
			continue

		elif menuchoice == "quit":
			break

		else:
			print("command unknow")
	print("see you soon...")

if u_id != identifiant and u_mdp != mdp:
	print("your id or password it's wrong, please, retry..")
	while u_id != identifiant and u_mdp != mdp:
		print("retry connection : ")
		u_id = input("enter your id : ")
		u_mdp = input("Enter your password : ")

	
	

	



