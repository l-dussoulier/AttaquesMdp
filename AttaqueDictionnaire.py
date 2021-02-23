import re, hashlib, sys, time

sys.stdout = open('result', 'w')

def affichage(result):
    print(result)

with open('shadow', 'r') as f:
   lines = f.readlines()


pwdTable = {}
for line in lines:
   try:
      user, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
   except IndexError:
      continue
   else:
      pwdTable[user]=user_hash

with open('dico_mini_fr', 'r') as f:
   lines = f.readlines()

for line in lines:
    debut = time.time()
    word=line.strip()
    current_hash = hashlib.md5(word.encode('utf')).hexdigest()
    for user, password in pwdTable.items():
        if current_hash == password:
            affichage("le code trouver pour l'utilisateur "+user+" est "+word)
            fin = time.time()
            result = time.localtime(fin-debut)
            print ("Trouver en : ",str(result.tm_sec)+" secondes")
