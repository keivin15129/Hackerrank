import long
def minion_game(s):
    # your code goes here
    player1=0
    player2=0
    vowels=['A','E','I','O','U']
   
    for i in range ( len( s)) :
        if s[i] not in vowels : 
            player1=player1 + 1
            for k in range (i+1,len(s)):
                player1=player1 + 1
        if s[i] in vowels : 
           player2 = player2 + 1
          # print player2,'PLAYER2'
           for k in range (i+1, len (s)):
                player2 = player2 + 1
          #      print player2,'PLAYER2'
    if player1>player2 : 
        print 'Stuart', player1
    elif player1<player2 : 
        print 'Kevin', player2
    else :
        print 'Draw'

  
















