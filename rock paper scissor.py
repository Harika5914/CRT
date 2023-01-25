#!/usr/bin/env python
# coding: utf-8

# In[1]:


#rock paper scissor game
from random import randint,random
choice=['rock','paper','scissor']
score1=0
score2=0
print('0 is rock  \n 1 is paper  \n2 is scissor')
while score1!=4 and score2!=4:
    
    player1=choice[int(input())]
    print('Player1 trial',player1)
    
    player2=choice[randint(0,2)]
    print('player2 trial',player2)
    if player1==player2:
        print('this is draw')
        continue
    if player1=='rock' and player2=='scissor':
        score1=score1+1
        print(score1,score2)
    elif player1=='paper' and player2=='rock':
        score1=score1+1 
        print(score1,score2)
    elif player1=='scissor' and player2=='paper':
        score1=score1+1
        print(score1,score2)
    else:
        score2=score2+1
        print(score1,score2)
if score1==4:
    print('player 1 wins')
else:
    print('player2 wins')


# In[ ]:




