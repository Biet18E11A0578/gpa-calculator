from termcolor import colored
print(colored("Semester 4 : ","blue"))

dbmslg = float(input('dbms lab Grades:'))
dbmslc = float(input('dbms lab credits:'))
dbmsl = dbmslg * dbmslc

javalg = float(input('java lab Grades:'))
javalc = float(input('java lab credits:'))
javal = javalg * javalc

oslg = float(input('os lab Grades:'))
oslc = float(input('os lab credits:'))
osl = oslg * oslc

coig = float(input('constitution of india Grades:'))
coic = float(input('constitution of india credits:'))
coi = coig * coic

befag = float(input('befa Grades:'))
befac = float(input('befa credits:'))
befa = befag * befac

dbmsg = float(input('dbms Grades:'))
dbmsc = float(input('dbms credits:'))
dbms = dbmsg * dbmsc

dmg = float(input('dm Grades:'))
dmc = float(input('dm credits:'))
dm = dmg * dmc

javag = float(input('java Grades:'))
javac = float(input('java credits:'))
java = javag * javac

ossg = float(input('os Grades:'))
ossc = float(input('os credits:'))
oss = ossg * ossc

total_point4 = (dbmsl + javal + osl + coi + befa + dbms + dm + java + oss)
total_credits4 = (dbmslc + javalc + oslc + coic + befac + dbmsc + dmc + javac + ossc)
sgpa22 = total_point4/total_credits4

'''
    print(total_point4)
    print(total_credits4)
'''
print(colored('Sem 4 - SGPA : ','green'))
print(colored(sgpa22,'yellow'))
print()

