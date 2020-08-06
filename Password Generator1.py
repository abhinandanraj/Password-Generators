from random import randint as r

acceptableChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
'U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
't','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&','*','(',
')',':']

pW = ['p','a','s','s','w','o','r','d',]

for i in range(8):
    pW[i] = acceptableChars[r(0,71)]
    
passWord = "{0}{1}{2}{3}{4}{5}{6}{7}". format(pW[0],pW[1],pW[2],pW[3],pW[4],pW[5],pW[6],pW[7])

print("Your password is: " + passWord)
