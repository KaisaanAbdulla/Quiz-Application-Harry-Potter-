import random
Red = "\u001b[31m"
Green = "\u001b[32m"
Blue = "\u001b[34m"

Positive = ['Well done!!!','Great job!!', 'Keep going your doing great', 'Nicely done' ]

count = 0
print (Blue +"                       Quiz Application                   ")
print (Green+"                         Harry Potter                      ")
def Q (question):
  return input(Red + question + Blue)

#---------------------------------------------------------

Q1 = Q("\nQuestion 1 : How many Harry Potter books are there? \na. 7\nb. 8 \nc. 11 \n \nWrite a, b or c\n")

     
if Q1 == '7' or Q1 == 'A' or Q1 == 'a' :  
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print (Red +"\nWrong answer :(")

print ("Your score is", count)

#---------------------------------------------------------

Q2 = Q ('\nQuestion 2 : Who are the gaurdians of Harry Potter after his parents died?\na. Lord Voldemort\nb. The Dursleys \nc. The Weaslys\n \nWrite a, b or c\n') 

if Q2 == 'B' or Q2 == '' or Q2 == 'b' :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print (Red +"\nWrong answer :(")

print ("Your score is", count)
 
#---------------------------------------------------------  

Q3 = Q ('\nQuestion 3 : What shape scar does Harry have on his forehead?\na. A Bucket\nb. A Lightning Bolt\nc. A Sun  \n \nWrite a, b, c\n') 
  
if Q3 == 'B' or Q3 == 'b'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 

Q4 = Q ('\nQuestion 4 : Who are Harry Potters 2 best friends?\na. Neville and Draco Malfoy\nb. Sirius Black and James Potter\nc. Hermione and Ron  \n \nWrite a, b, c\n') 
  
if Q4 == 'C' or Q4 == 'c'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1
  
else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#---------------------------------------------------------

Q5 = Q ('\nQuestion 5 : Which Hogwarts house is Harry in? \na. Gryffindor\nb. Slytherin\nc. Ravenclaw\n \nWrite a, b, c\n') 
  
if Q5 == 'A' or Q5 == 'a'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 
Q6 = Q ('\nQuestion 6 : Who is Harry Potters arch enemy? \na. Lord Voldemort\nb. Professor Severus Snape\nc. Draco Malfoy\n \nWrite a, b, c\n') 
  
if Q6 == 'A' or Q6 == 'a'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1
else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 
Q7 = Q ('\nQuestion 7 : What is the name of Harry Potters pet owl?\na. Snowy\nb. Crookshanks\nc. Hedwig \n \nWrite a, b, c\n') 
  
if Q7 == 'c' or Q7 == 'C'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 
Q8 = Q ('\nQuestion 8 : What is the core made of in Harry Potters wand?\na. Pheonix Feather\nb. Philosephers stone\nc. Diamond  \n \nWrite a, b, c\n') 
  
if Q8 == 'A' or Q8 == 'a'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1
  
else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 
Q9 = Q ('\nQuestion 9 : What is Harry Potter favorite sport?\na. Badminton\nb. Football\nc. Quidditch \n \nWrite a, b, c\n') 
  
if Q9 == 'C' or Q9 == 'c'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1
  
else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)


#--------------------------------------------------------- 
Q10 = Q ('\nQuestion 10 : Who killed Harry Potters parents?\na. Lucias Malfoy\nb. Lord Voldemort Potter\nc. Dolores Umbridge  \n \nWrite a, b, c\n') 
  
if Q10 == 'B' or Q10 == 'b'  :
  print( Green +  " \nCorrect!", (str(random.choice(Positive)))) 
  count = count+1

else:
   print ( Red +"\nWrong answer :(")

print ("Your score is", count)

#--------------------------------------------------------- 

i = count
while i > 7:
  print( Green + "\nYou are a Harry Potter fan")
  break

print(Blue + "\nThank you for playing the quiz")