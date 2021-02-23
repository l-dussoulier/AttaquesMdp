import re, itertools, hashlib, sys, datetime, time
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','_','#','0','1','2','3','4','5','6','7','8','9']
MAXLEN = 11
MINLEN = 5
string=""
taille=0

def redo(string,size):
    if taille <= MAXLEN:
        for i in alphabet:
            debut = time.time()
            tmpString=string+i
            tmpSize=taille+1
            redo(tmpString,tmpSize)
            if MINLEN <= len(tmpString):
                current_hash=hashlib.md5(tmpString.encode('utf')).hexdigest()
                if current_hash in pwdTable.values():
                    fin = time.time()
                    result = time.localtime(fin - debut)
                    affichage('mot de passe trouve \'{}\' pour l\'utilisateur {}'.format(tmpString, ','.join(i for i in pwdTable if pwdTable[i] == current_hash)))
                    affichage("Trouver en : " + str(result.tm_sec) + " secondes")



def affichage(s):
   print(s)

with open('shadow', 'r') as f:
    lines = f.readlines()

pwdTable = {}
for line in lines:
   try:
      user, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue
   else:
      pwdTable[user] = user_hash

affichage('\n'+str(len(pwdTable))+' Mot de passe chiffré sous MD5 trouvé, déchiffrage en cours entre '+str(MINLEN+1)+' et '+str(MAXLEN+1)+' caractères...\n')
redo(string,taille)