import pandas as pd
import random

random.seed(10)

num_of_question = 10;

df = pd.read_excel ('Kids800Voca.xlsx').to_dict()

total_vocab = len(df['영어단어'])
#번호	영어단어	단어 뜻	영어 문장	한국어 해석

kahoot = dict()
kahoot["Q"] = []#Question
kahoot["1"] = []#1
kahoot["2"] = []#2
kahoot["3"] = []#3
kahoot["4"] = []#4
kahoot["time"] = []#time limit
kahoot["A"] = []#Correct Answer

qlist = list(range(0,total_vocab-1))
random.shuffle(qlist)

q_count = 0
session_count=0

print('started\n')

for qn in qlist:
    kahoot["Q"].append(df['영어단어'][qn] + ": " + df['영어 문장'][qn])
    aidx = list(range(1,5))
    random.shuffle(aidx)
    kahoot[str(aidx[0])].append(df['단어 뜻'][qn])
    kahoot[str(aidx[1])].append(df['단어 뜻'][random.randint(0, total_vocab)])
    kahoot[str(aidx[2])].append(df['단어 뜻'][random.randint(0, total_vocab)])
    kahoot[str(aidx[3])].append(df['단어 뜻'][random.randint(0, total_vocab)])
    kahoot["time"].append(10000)
    kahoot["A"].append(aidx[0])
    q_count = q_count+1
    print('%d'%q_count)
    if q_count > num_of_question:
        q_count = 0
        pd.DataFrame(kahoot).to_excel('session%s.xls'%str(session_count))
        print('exporting session %s to session%s.xls\n'%(str(session_count),str(session_count)))
        kahoot.clear()
        kahoot["Q"] = []#Question
        kahoot["1"] = []#1
        kahoot["2"] = []#2
        kahoot["3"] = []#3
        kahoot["4"] = []#4
        kahoot["time"] = []#time limit
        kahoot["A"] = []#Correct Answer

        session_count = session_count+1       

