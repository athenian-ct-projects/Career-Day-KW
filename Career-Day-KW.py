#Career Quiz 
#KW '23 

#This asks the person's name and stores it so I am resuse it when I tell them their results
print("Hello! Welcome to the Career Aptitude Test!")
name = input("Enter your name: ")
print("Hi " + name + "!")
print("I hope you have a fun time doing this quiz (:")
print("If the game breaks it's probably your fault (:")


#All questions follow the same format: when the answer is a certian thing the corrosponding jobs get "points"
#The job with the most "points" at the end wins
#I am making the questions into a function so that I can call them again once the game is over, so that the play can play again

#this lets me add points to each outcome using a function

def addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,a,b,c,d,e,f,g,h,i):
  SoftwareDeveloper += a
  Physician += b
  Dentist += c
  Mathematician += d
  Accountant += e
  Landscaper += f
  Lawyer += g
  HairDresser += h
  TargetWorker += i
  scores=[SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker]
  return scores

#this sets the game as a function so I can recall it
def game ():
  #This sets up each possible outcome and allows me to add points to them when the player gives certain answers using the function
  SoftwareDeveloper = 0
  Physician = 0
  Dentist = 0
  Mathematician = 0
  Accountant = 0
  Landscaper = 0
  Lawyer = 0
  HairDresser = 0
  TargetWorker = 0
  x = 0

  #This is the first questions, all questions follow the same format
  #Question one
  answer1= input("Are you more interested in math, humanities, or science? ")
  if answer1 == "math":
    #this uses the aformentioned function to add points to the jobs (this is literally only used bc I had no other functions but it works so it's fine)
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,1,0,0,2,1,0,0,0,0)  
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if answer1 == "science":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,2,2,0,0,1,0,0,0)  
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if answer1 == "humanities":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,0,2,1,1)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8] 
  #This is incase the player spells something wrong or doesn't input an accepted value (this is repeated each time)
  while answer1 != "math" and answer1 != "science" and answer1 != "humanities":
    print("Oops! What you enetered doesn't work! Try again:")
    answer1 = input()

  #Question two
  answer2 = input("Do you want to work in a group environment in your future career? ")
  if answer2 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,1,1,0,0,0,1,1,1)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8] 
  while answer2 != "yes" and answer2 != "no":
    print("Oops! What you enetered doesn't work! You need a yes or no answer. Try again:")
    answer2 = input()

  #Question three
  print("DON'T ENTER ANY LETTERS OR COMMAS OR THE GAME WILL BREAK!!!") 
  answer3 = input("How much money do you want to make annually (between 20000 and 160000 dollars)? ")
  if int(answer3) >= 20000 and int(answer3) <= 20999:
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,0,0,0,1)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8] 
  if int(answer3) > 21000 and int(answer3) < 30000:
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,1,0,1,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if int(answer3) > 31000 and int(answer3) < 105000:
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,1,1,0,1,1,0,0,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if int(answer3) > 106000 and int(answer3) < 120000:
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,1,0,0,1,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if int(answer3) > 121000 and int(answer3) < 160000:
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,1,0,0,0,0,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while int(answer3) <= 19999 and int(answer3) > 161000: 
    print("Oops! What you entered doesn't work! You need an answer between 20000 and 160000. Try again:")
    answer3 = input()

  #Question four
  answer4 = input("Do you consider yourself academically intelligent? ")
  if answer4 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,2,2,1,2,1,0,2,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if answer4 == "no":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,0,0,5,5)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer4 != "yes" and answer4 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer4 = input()

  #Question five
  answer5 = input("Do you want to work in the medical field? ")
  if answer5 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,10,10,0,0,0,0,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer5 != "yes" and answer5 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer5 = input()

  #Question six
  answer6 = input("Do you want to work mainly inside or outside? ")
  if answer6 == "inside":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,1,1,1,1,1,0,1,1,1)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if answer6 == "outside":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,10,0,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer6 != "inside" and answer6 != "outside":
    print("Oops! What you entered doesn't work! You need to either enter inside or outside. Try again:")
    answer6 = input()

  #Question seven 
  answer7 = input("Do you want to work in customer service / work with people outside your company? ")
  if answer7 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,1,1,0,0,1,1,1,1)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer7 != "yes" and answer7 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer7 = input()

  #Question eight
  answer8 = input("Do you want a high prestige job? ")
  if answer8 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,1,1,1,1,0,0,1,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer8 != "yes" and answer8 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer8 = input()

  #Question nine
  answer9 = input("Are you planning on attending and graduating a four year university? ")
  if answer9 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,1,1,1,1,1,0,1,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer9 != "yes" and answer9 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer9 = input()

  #Question ten
  answer10 = input("Do you plan on attending and graduating from a graduate school")
  if answer10 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,1,1,1,1,0,1,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer10 != "yes" and answer10 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer10 = input()

  #Question eleven
  answer11 = input("Do you want to attend a cosmetology school? ")
  if answer11 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,0,0,0,100,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  while answer11 != "yes" and answer11 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer11 = input()

  #Question twelve
  answer12 = input("Do you want to work in a business enviroment? ")
  if answer12 == "yes":
    newScores = addToScore(SoftwareDeveloper,Physician,Dentist,Mathematician,Accountant,Landscaper,Lawyer,HairDresser,TargetWorker,0,0,0,0,1,0,1,0,0)
    SoftwareDeveloper=newScores[0]      
    Physician = newScores[1]
    Dentist = newScores[2]
    Mathematician = newScores[3]
    Accountant = newScores[4]
    Landscaper = newScores[5]
    Lawyer = newScores[6]
    HairDresser = newScores[7]
    TargetWorker = newScores[8]
  if answer12 != "yes" and answer12 != "no":
    print("Oops! What you entered doesn't work! You need a yes or no answer. Try again:")
    answer12 = input()

#This figures out which job has the most outright "points"
#Whichever job has the most "points" is announced as the players perfect job
#The x += 1 is so that the lower blocks checking for ties won't run 
#this can be done better but I didn't have time to redo it

  if SoftwareDeveloper > Physician and SoftwareDeveloper > Dentist and SoftwareDeveloper > Mathematician and SoftwareDeveloper > Accountant and SoftwareDeveloper > Landscaper and SoftwareDeveloper > Lawyer and SoftwareDeveloper > HairDresser and SoftwareDeveloper > TargetWorker:
    print("Congrats " + name + " your perfect job is a Software Developer!")
    x += 1
  if Physician > SoftwareDeveloper and Physician > Dentist and Physician > Mathematician and Physician > Accountant and Physician > Landscaper and Physician > Lawyer and Physician > HairDresser and Physician > TargetWorker:
    print("Congrats " + name + " your perfect job is a Physician!")
    x += 1
  if Dentist > SoftwareDeveloper and Dentist > Physician and Dentist > Mathematician and Dentist > Accountant and Dentist > Landscaper and Dentist > Lawyer and Dentist > HairDresser and Dentist > TargetWorker:
    print("Congrats " + name + " your perfect job is a Dentist!")
    x += 1
  if Mathematician > SoftwareDeveloper and Mathematician > Physician and Mathematician > Dentist and Mathematician > Accountant and Mathematician > Landscaper and Mathematician > Lawyer and Mathematician > HairDresser and Mathematician > TargetWorker:
    print("Congrats " + name + " your perfect job is a Mathematician!")
    x += 1
  if Accountant > SoftwareDeveloper and Accountant > Physician and Accountant > Dentist and Accountant > Mathematician and Accountant > Landscaper and Accountant > Lawyer and Accountant > HairDresser and Accountant > TargetWorker:
    print("Congrats " + name + " your perfect job is an Accountant!")
    x += 1
  if Landscaper > SoftwareDeveloper and Landscaper > Physician and Landscaper > Dentist and Landscaper > Mathematician and Landscaper > Accountant and Landscaper > Lawyer and Landscaper > HairDresser and Landscaper > TargetWorker:
    print("Congrats " + name + " your perfect job is a Landscaper!")
    x +=1 
  if Lawyer > SoftwareDeveloper and Lawyer > Physician and Lawyer > Dentist and Lawyer > Mathematician and Lawyer > Accountant and Lawyer > Landscaper and Lawyer > HairDresser and Lawyer > TargetWorker:
    print("Congrats " + name + " your perfect job is a Lawyer!")
    x += 1
  if HairDresser > SoftwareDeveloper and HairDresser > Physician and HairDresser > Dentist and HairDresser > Mathematician and HairDresser > Accountant and HairDresser > Landscaper and HairDresser > Lawyer and HairDresser > TargetWorker:
    print("Congrats " + name + " your perfect job is a Hair Dresser!")
    x += 1
  if TargetWorker > SoftwareDeveloper and TargetWorker > Physician and TargetWorker > Dentist and TargetWorker > Mathematician and TargetWorker > Accountant and TargetWorker > Landscaper and TargetWorker > Lawyer and TargetWorker > HairDresser:
    print("Congrats " + name + " your perfect job is a Target Worker!")
    x += 1


#This is incase two jobs have the same amount of "points"
#The code asks a final question and then gives a "winning" job
  if x == 0:
    if SoftwareDeveloper == Physician:
      x += 1
      SoftwarePhysiciantie = input("Do you like computers or medicine more? ")
      if SoftwarePhysiciantie == "computers":
        print("Congrats " + name + " a good job for you would be a Software Developer!")
      if SoftwarePhysiciantie == "medicine":
        print("Congrats " + name + " a good job for you would be a Physician!")
      #This is incase the player misspells somethign or doesn't input an accepted value
      while SoftwarePhysiciantie != "medicine" and SoftwarePhysiciantie != "computers":
        print("Oops! What you entered doesn't work! You need to either answer computers or medicine. Try again:")
        SoftwarePhysiciantie = input()

#These blocks of code all follow the same format, and only get run incase two jobs are tied
#This block only runs when x == 0 so and changes x to 1 once it has been run, that way it won't be able to ask you two questions / give you two jobs
  if x == 0:
    if SoftwareDeveloper == Dentist:
      x += 1
      SoftwareDentisttie = input("Do you like teeth or computers more?") 
      if SoftwareDentisttie == "teeth":
        print("Congrats " + name + " a good job for you would be a Dentist!")
      if SoftwareDentisttie == "computers":
        print("Congrats " + name + " a good job for you would be a Software Developer!")
      while SoftwareDentisttie != "computers" and SoftwareDentisttie != "teeth":
        print("Oops! What you entered doesn't work! You need to either answer computers or teeth. Try again:")
        SoftwareDentisttie = input()
 
  if x == 0:
    if SoftwareDeveloper == Mathematician:
      x += 1
      SoftwareMathtie = input("Do you like coding or solving equations more? ")
      if SoftwareMathtie == "coding":
        print("Congrats " + name + " a good job for you would be a Software Developer!")
      if SoftwareMathtie == "solving equations":
        print("Congrats " + name + " a good job for you would be a Mathematician!")
      while SoftwareMathtie != "coding" and SoftwareMathtie != "solving equations":
        print("Oops! What you entered doesn't work! You need to either answer coding or solving equations. Try again:")
        SoftwareMathtie = input()

  if x == 0:
    if SoftwareDeveloper == Accountant:
      x += 1
      SoftwareAccounttie = input("Do you like computers or doing taxes more? ")
      if SoftwareAccounttie == "computers":
        print("Congrats " + name + " a good job for you would be a Software Developer!")
      if SoftwareAccounttie == "doing taxes":
        print("Congrats " + name + " a good job for you would be an Accountant!")
      while SoftwareAccounttie != "computers" and SoftwareAccounttie != "doing taxes":
        print("Oops! What you entered doesn't work! You need to either answer computers or doing taxes. Try again:")
        SoftwareAccounttie = input()

  if x == 0:
    if SoftwareDeveloper == Lawyer:
      x += 1
      SoftwareLawtie = input("Do you like law or coding more? ")
      if SoftwareLawtie == "law":
        print("Congrats " + name + " a good job for you would be a Lawyer!")
      if SoftwareLawtie == "coding":
        print("Congrats " + name + " a good job for you would be a Software Developer!")
      while SoftwareLawtie != "coding" and SoftwareLawtie != "law":
        print("Oops! What you entered doesn't work! You need to either answer coding or law. Try again:")
        SoftwareLawtie = input()

  if x == 0:
    if Physician == Dentist:
      x += 1
      PhysicianDentisttie = input("Do you like teeth or blood more? ")
      if PhysicianDentisttie == "teeth":
        print("Congrats " + name + " a good job for you would be a Dentist!")
      if PhysicianDentisttie == "blood":
        print("Congrats " + name + " a good job for you would be a Physician!")
      while PhysicianDentisttie != "teeth" and PhysicianDentisttie != "blood":
        print("Oops! What you entered doesn't work! You need to either answer teeth or blood. Try again:")
        PhysicianDentisttie = input()

  if x == 0:
    if Physician == Mathematician:
      x += 1
      PhysicianMathtie = input("Do you like biology or math more? ")
      if PhysicianMathtie == "biology":
        print("Congrats " + name + " a good job for you would be a Physician!")
      if PhysicianMathtie == "math":
        print("Congrats " + name + " a good job for you would be a Mathematician!")
      while PhysicianMathtie != "biology" and PhysicianMathtie != "math":
        print("Oops! What you entered doesn't work! You need to either answer biology or math. Try again:")
        PhysicianMathtie = input()

  if x == 0:
    if Physician == Accountant:
      x += 1
      PhysicianAcctie = input("Do you like blood or doing taxes more? ")
      if PhysicianAcctie == "blood":
        print("Congrats " + name + " a good job for you would be a Physician!")
      if PhysicianAcctie == "doing taxes":
        print("Congrats " + name + " a good job for you would be an Accountant!")
      while PhysicianAcctie != "blood" and PhysicianAcctie != "doing taxes":
        print("Oops! What you entered doesn't work! You need to either answer blood or doing taxes. Try again:")
        PhysicianAcctie = input()

  if x == 0:
    if Physician == Lawyer:
      x += 1
      PhysicianLawtie = input("Do you like biology or law more? ")
      if PhysicianLawtie == "biology":
        print("Congrats " + name + " a good job for you would be a Physician!")
      if PhysicianLawtie == "law":
        print("Congrats " + name + " a good job for you would be a Lawyer!")
      while PhysicianLawtie != "biology" and PhysicianLawtie != "law":
        print("Oops! What you entered doesn't work! You need to either answer biology or law. Try again:")
        PhysicianLawtie = input()

  if x == 0:
    if Dentist == Mathematician:
      x += 1
      DentistMathtie = input("Do you like teeth or solving equations more? ")
      if DentistMathtie == "teeth":
        print("Congrats " + name + " a good job for you would be a Dentist!")
      if DentistMathtie == "solving equations":
        print("Congrats " + name + " a good job for you would be a Mathematician !")
      while DentistMathtie != "teeth" and DentistMathtie != "solving equations":
        print("Oops! What you entered doesn't work! You need to either answer teeth or solving equations. Try again:")
        DentistMathtie = input()
 
  if x == 0:
    if Dentist == Accountant:
      x +=1
      DentistAccounttie = input("Do you like teeth or doing taxes more?")
      if DentistAccounttie == "teeth":
        print("Congrats " + name + " a good job for you would be a Dentist!")
      if DentistAccounttie == "doing taxes":
        print("Congrats " + name + " a good job for you would be an Accountant!")
      while DentisrAccounttie != "teeth" and DentistAccounttie != "doing taxes":
        print("Oops! What you entered doesn't work! You need to either answer teeth or doing taxes. Try again:")
        DentistAccounttie = input()

  if x == 0:
    if Dentist == Lawyer:
      x +=1
      DentistLawyertie = input("Do you like medicine or law more?")
      if DentistLawyertie == "medicine":
        print("Congrats " + name + " a good job for you would be a Dentist!")
      if DentistLawyertie == "law":
        print("Congrats " + name + " a good job for you would be a Lawyer!")
      while DentistLawyertie != "medicine" and DentistLawyertie != "law":
        print("Oops! What you entered doesn't work! You need to either answer teeth or law. Try again:")
        DentistLawyertie = input()

  if x == 0:
    if Mathematician == Accountant:
      x += 1
      MathAccounttie = input("Do you like solving equations or doing taxes more?")
      if MathAccounttie == "solving equations":
        print("Congrats " + name + " a good job for you would be a Mathematician !")
      if MathAccounttie == "doing taxes":
        print("Congrats " + name + " a good job for you would be an Accountant!")
      while MathAccounttie != "solving equations" and MathAccounttie != "doing taxes":
        print("Oops! What you entered doesn't work! You need to either answer solving equations or doing taxes. Try again:")
        MathAccounttie = input()

  if x == 0:
    if Mathematician == Lawyer:
      x += 1
      MathLawtie = input("Do you like solving formulas or law more?")
      if MathLawtie == "solving formulas":
        print("Congrats " + name + " a good job for you would be a Mathematician !")
      if MathLawtie == "law":
        print("Congrats " + name + " a good job for you would be a Lawyer!")
      while MathLawtie != "solving equations" and MathLawtie != "law":
        print("Oops! What you entered doesn't work! You need to either answer solving equations or law. Try again:")
        MathLawtie = input()

  if x == 0:
    if Accountant == Lawyer:
      x += 1
      AccountLawtie = input("Do you like doing taxes or going to jury duty more more?")
      if AccountLawtie == "doing taxes":
        print("Congrats " + name + " a good job for you would be an Accountant!")
      if AccountLawtie == "going to jury duty":
        print("Congrats " + name + " a good job for you would be a Lawyer!")
      while AccountLawtie != "doing taxes" and AccountLawtie != "going to jury duty":
        print("Oops! What you entered doesn't work! You need to either answer solving equations or law. Try again:")
        AccountLawtie = input()

  if x == 0:
    if HairDresser == TargetWorker:
      x += 1
      HairTargettie = input("Do you like doing braiding hair or wearing red more?")
      if HairTargettie == "braiding hair":
        print("Congrats " + name + " a good job for you would be a Hair Stylist!")
      if HairTargettie == "wearing red":
        print("Congrats " + name + " a good job for you would be a Target Worker!")
      while HairTargettie != "braiding hair" and HairTargettie != "wearing red":
        print("Oops! What you entered doesn't work! You need to either answer braiding hair or wearing red. Try again:")
        HairTargettie = input()
  
  #this prints out the players scores incase they want to see them (or incase I want to check if the game is working) 
  print("do you want to see your scores? ")
  seescore = input("")
  if seescore == "yes":
    print("Software Developer: " + str(SoftwareDeveloper))
    print("Physician: " + str(Physician))
    print("Dentist: " + str(Dentist))
    print("Mathemtician: " +str(Mathematician))
    print("Accountant: " + str(Accountant))
    print("Landscaper: " + str(Landscaper))
    print("Lawyer: " + str(Lawyer))
    print("Hair Dresser: " + str(HairDresser))
    print("Target Worker: " + str(TargetWorker))
  if seescore != "yes" and seescore != "no":
    print("type yes or no")
    seescore = input("")


#This is incase the player wants to take the quiz again
#this sets playagain to "yes" and while that equals "yes" the game plays, so if the player says "no" the game ends
playagain='yes'

while playagain != "no":
  game()
  playagain = input("Do you want to play again? ")
print("ok cool bye " + name + "!")
for x in range (3): #this is only here because I needed a for loop and there was no logical place to put one
  print("yay!")
