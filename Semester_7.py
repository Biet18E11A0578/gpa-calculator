from termcolor import colored
print(colored("Semester 7 :","blue"))

cnslg = float(input('cns lab Grades:'))
cnslc = float(input('cns lab credits:'))
cnsl = cnslg * cnslc

seminarg = float(input('seminarGrades:'))
seminarc = float(input('seminar credits:'))
seminar = seminarg * seminarc

minig = float(input('mini Grades:'))
minic = float(input('mini credits:'))
mini = minig * minic

ps1g = float(input('ps1 Grades:'))
ps1c = float(input('ps1 credits:'))
ps1 = ps1g * ps1c

ccg = float(input('cc Grades:'))
ccc = float(input('cc credits:'))
cc = ccg * ccc
    
cnsg = float(input('cns Grades:'))
cnsc = float(input('cns credits:'))
cns = cnsg * cnsc

dmgg = float(input('dmg Grades:'))
dmgc = float(input('dmg credits:'))
dmg = dmgg * dmgc
    
sppmg = float(input('sppm Grades:'))
sppmc = float(input('sppm credits:'))
sppm = sppmg * sppmc

esg = float(input('es Grades:'))
esc = float(input('es credits:'))
es = esg * esc

total_point7 = (cnsl + seminar + mini + ps1 + cc + cns + dmg + sppm + es)
total_credits7 = (cnslc + seminarc + minic + ps1c + ccc + cnsc + dmgc + sppmc + esc)
sgpa41 = total_point7/total_credits7
'''
        print(total_point7)
        print(total_credits7)
'''
print(colored('Sem 7 - SGPA : ','green'))
print(colored(sgpa41,'yellow'))
print()


