import random
q1='''AThe language of Lakshadweep. a Union Territory of India, is
A - Malayalam
B - Hindi
C - English
D - Telugu
'''
q2='''BBahubali festival is related to
A - Islam
B - Jainism
C - Buddhism
D - Hinduism
'''
q3='''CThe death anniversary of which of the following leaders is observed as Martyrs' Day?
A - Smt. Indira Gandhi
B - Pt. Jawaharlal Nehru
C - Mahatma Gandhi
D - Lal Bahadur Shastri
'''
q4='''DPongal is a popular festival of which state?
A - Karnataka
B - Kerala
C - Andhra Pradesh
D - Tamil Nadu
'''
q5='''AGhototkach in Mahabharat was the son of
A - Bhima
B - Arjuna
C - Yudhishthir
D - Duryodhana
'''
q6='''BWhich of the following Muslim festivals is based on the "Holy Quran" ?
A - Id -ul-Fitr
B - Id -ul-Zuha
C - Bakri-id
D - Moharram
'''
q7='''CIn Mahabharat Kunti had how many sons?
A - 6
B - 5
C - 4
D - 3
'''
q8='''DVan Mahotsav was started by
A - Maharshi Karve
B - Bal Gangadhar Tiiak
C - Sanjay Gandhi
D - K.M, Munshi
'''
q9='''AWhich of the following is not a dance from Kerala?
A - Yaksha Gana
B - Mohiniattam
C - Ottan Thullal
D - Kathakali
'''
q10='''BThe first month of the Indian national calendar is
A - Magha
B - Chaitra
C - Ashadha
D - Vaishakha
'''
h1='''AThe festival of Nabanna is celebrated predominately in
A - Orissa
B - Rajasthan
C - Kamataka
D - Andhra Pradesh
'''
h2='''BThe Lalit Kala Academy is devoted to the promotion of
A - Dance & Drama
B - Fine Arts
C - Literature
D - Music
'''
h3='''CWhich of the following is a folk dance of India?
A - Kathakali
B - Mohiniattam
C - Garba
D - Manipuri
'''
h4='''DWhich one of the following is essentially a solo dance? 
A - Kuchipudi
B - Kathak
C - Manipuri
D - Mohiniattam
'''
h5='''DCentral Salt and Marine Chemicals Research Institute is located at
A - Ahmedabad
B - Bhavnagar
C - Gandhinagar
D - Panaji
'''
h5='''CWhich city of India was first of all affected by plague?
A - Jaipur
B - Bombay
C - Surat
D - Kanpur
'''
h6='''DWriters Building is the headquarters of
A - The times of India group
B - All India Writers Association
C - West Bengal Government
D - Press Trust of India
'''
h7='''AThe Komark Temple is dedicated to
A - Sun- God
B - Shiva
C - Krishna
D - Vishnu
'''
h8='''BThe 227 year old 'Nawab Saheb Ki Haveli' is Iocated at
A - Hyderabad
B - Jaipur
C - New Delhi
D - Agra
'''
h9='''CThe BVO (Brominated Vegetable Oil) was banned in soft drinks by which of the following organisations?
A - I.S.I.
B - AGMARK
C - MRTPC
D - None of These
'''
h10='''AThe abbreviation 'fob' stands for
A - Free on Board
B - Free of Bargain
C - Fellow of Britain
D - Noneof these
'''
i1='''DWhich of the following was the first Indian state to issue photo identity cards to its voters?
A - Tamil Nadu
B - Rajasthan
C - West Bengal
D - Haryana
'''
i2='''CThe value of π (Pai) was first given by
A - Bhaskara
B - Varahamihira
C - Aryabhatta
D - Ramanujan
'''
i3='''BThe conspiracy angle, of Rajiv Gandhi murder is being probed by
A - Mirdha Commission
B - Jain Commission
C - Chelliah Commission
D - Rangarajan Commmission
'''
i4='''CThe activists of which of the following movements gave a call to their members to take 'Jal Samadhi' in order to press thier demands?
A - Naxalite Movement
B - Chipko Movement
C - Narmada Bachao Andolan
D - Jharkhand Movement
'''
i5='''DThe Eendu newspapers is published from
A - Orissa
B - Kerala
C - Karnataka
D - Andhra Pradesh
'''
i6='''AWhich of the following European countries is the first buyer of Maruti Cars?
A - Hungary
B - Belgium
C - England
D - Spain
'''
i7=''' DIn which one of the following sets of countries does nuclear power account for more than or nearly 30 percent of the total electricity generated?
A - Japan, Chiria, Taiwan, North Korea
B - Japan, China, South Korea
C - Taiwan, North Korea, China, South Korea
D - Japan, Taiwan, South Korea
'''
i8='''DThe Thakkar Commission was appointed to investigate into the
A - Bofors deal
B - Centre State relations
C - Operation Blue Star
D - Indira Gandhi assassination Case
'''
i9='''DMost 'ancient musical' instrument among the following is
A - Sarod
B - Tabla
C - Sitar
D - Veena
'''
i10='''ClSI stands for
A - International Standards Institute
B - IndianStatisticaI Institute
C - Indian Standards Institute
D - Indian Service Institute
'''
lifeline_easy=['AUDIENCE POLL','5050']
lifeline_hard=['DOUBLE DIP','POWER PAPLU',]
lifeline_intermediate=['CHANGE THE QUESTION']
def ap(x):
    if x=='A':
        print('A - 60%')
        print('B - 20%')
        print('C - 15%')
        print('D - 5%')
    elif x=='B':
        print('A - 20%')
        print('B - 60%')
        print('C - 15%')
        print('D - 5%')
    elif x=='C':
        print('A - 20%')
        print('B - 15%')
        print('C - 60%')
        print('D - 5%')
    elif x=='D':
        print('A - 20%')
        print('B - 5%')
        print('C - 15%')
        print('D - 60%')

def fifty_fifty(z):
    if z=="A":
        print('CHOOSE FROM A AND D')
    if z=='B':
        print('CHOOSE FROM B AND D')
    if z=='C':
        print('CHOOSE FROM B AND C')
    if z=='D':
        print('CHOOSE FROM B AND D')

wallet=0
score=0
col=['A','B','C','D']
lqe=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
lqh=[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10]
lqi=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
#Level 1
print('LEVEL 1 QUESTIONS...')
i=1
while score!=7:
    print('QUESTION',i)
    i=i+1
    q=random.choice(lqe)
    lqe.remove(q)
    print(q[1:])
    correct_option=q[0]
    a=input('TYPE YOUR CHOICE - ').upper()
    if a=='LIFELINE':
        if len(lifeline_easy)==0:
            print('NO LIFELINE LEFT')
            a = input('TYPE YOUR CHOICE - ').upper()
        else:
            print(lifeline_easy)
            li = input('CHOOSE A LIFELINE - ').upper()
            if li=='AUDIENCE POLL':
                ap(correct_option)
                lifeline_easy.remove('AUDIENCE POLL')
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li=='5050':
                fifty_fifty(correct_option)
                lifeline_easy.remove('5050')
                a = input('TYPE YOUR CHOICE - ').upper()
    if a in col:
        if a == correct_option:
            print('CORRECT ANSWER')
            score = score + 1
            wallet=wallet+1000
        else:
            print('WRONG ANSWER, CORRECT ANSWER IS', correct_option)
            print('YOU EARNED -',wallet,'RUPEES')
            quit()


#LEVEL 2
print('LEVEL 2 QUESTIONS...')
lifeline_intermediate=lifeline_intermediate+lifeline_easy
score=0
i=1
while score!=7:
    print('QUESTION',i)
    i=i+1
    q=random.choice(lqi)
    lqi.remove(q)
    print(q[1:])
    correct_option=q[0]
    a=input('TYPE YOUR CHOICE - ').upper()
    if a=='LIFELINE':
        if len(lifeline_intermediate)==0:
            print('NO LIFELINE LEFT')
            a = input('TYPE YOUR CHOICE - ').upper()
        else:
            print(lifeline_intermediate)
            li = input('CHOOSE A LIFELINE - ').upper()
            if li=='AUDIENCE POLL':
                ap(correct_option)
                lifeline_intermediate.remove('AUDIENCE POLL')
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li=='5050':
                fifty_fifty(correct_option)
                lifeline_intermediate.remove('5050')
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li=='CHANGE THE QUESTION':
                lifeline_intermediate.remove('CHANGE THE QUESTION')
                q = random.choice(lqi)
                lqi.remove(q)
                print(q[1:])
                correct_option = q[0]
                a = input('TYPE YOUR CHOICE - ').upper()

    if a in col:
        if a == correct_option:
            score = score + 1
            wallet=wallet+10000
            print('CORRECT ANSWER')
        else:
            print('WRONG ANSWER, CORRECT ANSWER IS', correct_option)
            print('YOU EARNED -',wallet,'RUPEES')
            quit()

#LEVEL 3
print('LEVEL 3 QUESTIONS...')
lifeline_hard = lifeline_intermediate + lifeline_hard
score=0
i = 1
while score != 7:
    print('QUESTION', i)
    i = i + 1
    q = random.choice(lqh)
    lqh.remove(q)
    print(q[1:])
    correct_option = q[0]
    a = input('TYPE YOUR CHOICE - ').upper()
    if a == 'LIFELINE':
        if len(lifeline_hard) == 0:
            print('NO LIFELINE LEFT')
            a = input('TYPE YOUR CHOICE - ').upper()
        else:
            print(lifeline_hard)
            li = input('CHOOSE A LIFELINE - ').upper()
            if li == 'AUDIENCE POLL':
                ap(correct_option)
                lifeline_hard.remove('AUDIENCE POLL')
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li == '5050':
                fifty_fifty(correct_option)
                lifeline_hard.remove('5050')
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li == 'CHANGE THE QUESTION':
                lifeline_hard.remove('CHANGE THE QUESTION')
                q = random.choice(lqi)
                lqi.remove(q)
                print(q[1:])
                correct_option = q[0]
                a = input('TYPE YOUR CHOICE - ').upper()
            elif li=='POWER PALPU':
                print(['AUDIENCE POLL','5050','CHANGE THE QUESTION'])
                z=input('FROM THE ABOVE LIST WHICH LIFELINE YOU WANT TO REVIVE - ')
                if z == 'AUDIENCE POLL':
                    ap(correct_option)
                    a = input('TYPE YOUR CHOICE - ').upper()
                elif z == '5050':
                    fifty_fifty(correct_option)
                    a = input('TYPE YOUR CHOICE - ').upper()
                elif a == 'CHANGE THE QUESTION':
                    q = random.choice(lqi)
                    lqi.remove(q)
                    print(q[1:])
                    correct_option = q[0]
                    a = input('TYPE YOUR CHOICE - ').upper()
            elif li=='DOUBLE DIP':
                    w=input('ENTER YOUR FIRST CHOICE - ')
                    if w==correct_option:
                        score=score+1
                        wallet=wallet+100000
                        print('CORRECT ANSWER')
                        continue
                    else:
                        print('YOUR FIRST CHOICE IS WRONG')
                        w = input('ENTER YOUR SECOND CHOICE CHOICE - ')
                        if w == correct_option:
                            score = score + 1
                            wallet = wallet + 100000
                            print('CORRECT ANSWER')
                            continue
                        else:
                            print('YOUR SECOND CHOICE IS WRONG AND CORRECT ANSWER IS',correct_option)
                            print('YOU EARNED -',wallet,'RUPEES')
                        quit()
    if a in col:
        if a == correct_option:
            score = score + 1
            wallet=wallet+100000
            print('CORRECT ANSWER')
        else:
            print('WRONG ANSWER, CORRECT ANSWER IS', correct_option)
            print('YOU EARNED -',wallet,'RUPEES')
            quit()
