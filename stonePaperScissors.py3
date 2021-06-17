import random
#import turtle

def game():
	user=0
	sys=0	
	n=input("Enter your choice (s:stone , p:paper , c:scissors , q: quit):)\t")
	while n!='q' :
		flag=0
		comp=random.randrange(0,3)
		# 0: stone
		# 1: paper
		# 2: scissors
		if (comp==0 and n=='p'):		#stone v/s paper
			user+=1 				
			flag=1
		elif (comp==0 and n=='c'):		#stone v/s scissors
			sys+=1
		elif (comp==1 and n=='s'):		#paper v/s stone
			sys+=1
		elif (comp==1 and n=='c'):		#paper v/s scissors
			user+=1
			flag=1
		elif (comp==2 and n=='s'):		#scissors v/s  stone
			user+=1
			flag=1
		elif (comp==2 and n=='p'):		#scissors v/s paper
			sys+=1
		else :
			continue
		#
		#
		if flag==1:
			print("Congo user, it's your point :)\n")
		else :
			print("Alas!! it's the computer's point :(\n")
		#
		#
		n=input("Enter your choice (s:stone , p:paper , c:scissors , q: quit):)\t")
	return (user,sys)	
		
			
#win=turtle.Screen()
#alex=turtle.Turtle()
print("\n\n\t\tSTONE PAPER SCISSORS\n\n")
n=input("Enter your good name:\t")
usr,syst=game()
print("\n"+n+":"+str(usr))
print("System:"+str(syst)+"\n")
if (usr>syst) :
	print("\nCongratutions "+n+" you won the game :) ;)\n")
elif (usr<syst) :
	print("\nSorry system won the game :)\nBetter Luck next Time :)\n")
else :
	print("\nIt's a Tie !!! \n")
