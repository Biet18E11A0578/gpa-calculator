from termcolor import colored
print(colored("Semester 5 :","blue"))

acslg = float(input('acs lab Grades:'))
acslc = float(input('acs lab credits:'))
acsl = acslg * acslc

cnwtlg = float(input('cnwt lab Grades:'))
cnwtlc = float(input('cnwt lab credits:'))
cnwtl = cnwtlg * cnwtlc

selg = float(input('se lab Grades:'))
selc = float(input('se lab credits:'))
sel = selg * selc

iprg = float(input('ipr Grades:'))
iprc = float(input('ipr credits:'))
ipr = iprg * iprc

aig = float(input('ai Grades:'))
aic = float(input('ai credits:'))
ai = aig * aic

cgsg = float(input('cg Grades:'))
cgsc = float(input('cg credits:'))
cgs = cgsg * cgsc

cng = float(input('cn Grades:'))
cnc = float(input('cn credits:'))
cn = cng * cnc

dag = float(input('da Grades:'))
dac = float(input('da credits:'))
da = dag * dac

flatg = float(input('flat Grades:'))
flatc = float(input('flat credits:'))
flat = flatg * flatc

seg = float(input('se Grades:'))
sec = float(input('se credits:'))
se = seg * sec

wtg = float(input('wt Grades:'))
wtc = float(input('wt credits:'))
wt = wtg * wtc

total_point5 = (acsl + cnwtl + sel + ipr + ai + cgs + cn + da + flat + se + wt)
total_credits5 = (acslc + cnwtlc + selc + iprc + aic + cgsc + cnc + dac + flatc + sec + wtc)
sgpa31 = total_point5/total_credits5

'''
        print(total_point5)
        print(total_credits5)
'''
print(colored('Sem 5 - SGPA : ','green'))
print(colored(sgpa31,'yellow'))
print()

