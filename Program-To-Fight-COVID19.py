print("Welcome to the quiz/game to fight corona virus. This program is made to spread awareness to the whole world about corona virus and what precautions should be take to fight corona virus")
print("This is a quiz game in which you need to answer few questions about how we can save ourselves and others form corona virus. You will also get marks for answering all the questions correctly")
score = 0
total_q = 10
ans=str(input("Do you want to play this quiz game? (type yes/no):"))
if ans=='no':
    print("Please don't quit like this only. Please play this game at least once.")
    quit()
if ans=='yes':
    print("Thanks for starting this quiz/game. So,let's get started. ")
else:
    print("Only type yes or no")
    quit()


a=str(input("1:- Can corona Virus spread form one preson to other? (type yes/no):"))
if a=='yes':
    score += 1  
    print("That's absolutely correct!")
else:
    print("Your answer is wrong. The correct answer is Yes.")


b=str(input("2:- Nowadays you are seeing that in some people corona does not show any symptoms. Is this sentence true about corona virus?(type true/false):"))    
if b=='true':
    score += 1
    print("That's absolutely correct!")
else:
     print("Your answer is wrong. The correct answer is true.")


c=str(input("3:- How can we protect ourselves form corona virus? Options are a:-By Not wearing mask  b:- By doing handshake with everyone c:- By wearing mask and not doing handshake with anyone(type a , b , c. You have to type and one option form the above.)"))     
if c=='c':
     score += 1
     print("That's absolutely correct!")
else:
     print("Your answer is wrong. The correct answer is c.")

 
d=str(input("4:- Do you know that what are the symptoms of corona virus? (type yes/no):"))
if d=='yes':
    score += 1
    print("That's pretty good if you know that what are the symptoms of corona virus.")
if d=='no':
    print("OK that's not a big deal,if you don't know the  symptoms of corona virus but you should know them. Ok now I will tell you the symptoms of corona virus. The symptoms of corona virus are as follow:-")
    print("Common symptoms: Fever , Tiredness , DryCough")
    print("Some people may also experince the following symptoms:- ")
    print("aches and pains , nasal congestion , runny nose , sore throat , diarrhoea. ")
    print("So, these were the symptoms of corona virus.")

    
e=str(input("5:- Do you know that what is the name given to corona virus ?(type yes/no). if you will type yes then also type the name also:"))
if e=='yes COVID-19':
    score += 1 
    print("That's absolutely correct!")
else:
     print("Your answer is wrong. The correct answer is COVID-19.")


f=str(input("6:- To which age people corona virus catches very fastly? Options are a:- Childhood age b:- Adulthood age c:- Old age d:- Both childhhod age and Old age. (type a , b , c , d):"))
if f=='d':
     score += 1 
     print("That's absolutely correct!")
else:
    print("Your answer is wrong. The correct answer is d.")


g=str(input("7:- To whom did Brazil gave the name of Hanuman ji?"))
if g=='Narendra Modi Ji':
    score += 1
    print("That's absolutely correct!")
elif g=='narendra modi ji':
    score += 1
    print("That's absolutely correct!")
elif g=='narendra modi ':
    score += 1
    print("That's absolutely correct!")
elif g=='narendra Modi Ji':
    score += 1
    print("That's absolutely correct!")
elif g=='narendra Modi ji':
    score += 1
    print("That's absolutely correct!")
elif g=='Narendra Modi ji':
    score += 1
    print("That's absolutely correct!")
elif g=='Narendra modi ji':
    score += 1
    print("That's absolutely correct!")
else:
    print("Your answer is wrong. The correct answer is Narendra Modi Ji.")


h=str(input("8:- Do you know that how many days corona virus takes to show its symptoms in a person having corona virus?(type yes/no):"))
if h=='yes':
    score += 1
    print("Ok that's very good.")
if h=='no':
    print("Ok if you don't know that how many days corona virus takes to show its symptoms in a person having corona virus then I will tell you")
    print("On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.")


i=str(input("9:- Nowadays a person is the superhero fo the whole India and even the whole world. Can you name that person?"))
if i=='Narendra Modi Ji':
    score += 1
    print("That's absolutely correct!")
elif i=='narendra modi ji':
    score += 1
    print("That's absolutely correct!")
elif i=='narendra modi':
    score += 1
    print("That's absolutely correct!")
elif i=='Narendra modi':
    score += 1
    print("That's absolutely correct!")
elif i=='Narendra Modi':
    score += 1
    print("That's absolutely correct!")
elif i=='narendra Modi':
    score += 1
    print("That's absolutely correct!")
elif i=='Narendra modi ji':
    score += 1
    print("That's absolutely correct!")
elif i=='narendra Modi Ji':
    score += 1
    print("That's absolutely correct!")
elif i=='narendra Modi ji':
    score += 1
    print("That's absolutely correct!")
elif i=='Narendra Modi ji':
    score += 1
    print("That's absolutely correct!")
elif i=='Narendra modi Ji':
    score += 1
    print("That's absolutely correct!")    
else:
    print("Your answer is wrong. The correct answer is Narendra Modi Ji ")
    


j=str(input("10:- How did corona virus came to India? Options are a:-International Flights b:- From other States (type a , b): "))
if j=='a':
    score += 1
    print("That's absolutely correct!")
else:
    print("Your answer is wrong. The correct answer is a")


    
    
print("Thanks a lot for playing this qiz/game. We hope you enjoyed a lot. We request you please don't go out of your houses and stay safe from corona virus and follow all the guidelines of the government.")
print("let's take a pledge toghter to fight corona virus and make corona virus defeat.")
print("Salute to all our heros who stay outdoor for us only. So , can't we stay indoor for them only. Please stay home. This is our Humble request to you.")
print('you got ',score,"questions correct.")
mark = (score/total_q) * 100
print("Mark: ", mark)
print("Good Bye")
print("STAY HOME STAY SAFE!")





    

    
    
