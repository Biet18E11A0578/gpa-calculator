from termcolor import colored
print(colored("Semester 6 : ","blue"))

cdlg = float(input('cd lab Grades:'))
cdlc = float(input('cd lab credits:'))
cdl = cdlg * cdlc

mllg = float(input('ml lab Grades:'))
mllc = float(input('ml lab credits:'))
mll = mllg * mllc

stmlg = float(input('stm lab Grades:'))
stmlc = float(input('stm lab credits:'))
stml = stmlg * stmlc

csg = float(input('cs Grades:'))
csc = float(input('cs credits:'))
cs = csg * csc

cdg = float(input('cd Grades:'))
cdc = float(input('cd credits:'))
cd = cdg * cdc

daag = float(input('daa Grades:'))
daac = float(input('daa credits:'))
daa = daag * daac

mlg = float(input('ml Grades:'))
mlc = float(input('ml credits:'))
ml = mlg * mlc

stmg = float(input('stm Grades:'))
stmc = float(input('stm credits:'))
stm = stmg * stmc

foitg = float(input('foit Grades:'))
foitc = float(input('foit credits:'))
foit = foitg * foitc

total_point6 = (cdl + mll + stml + cs + cd + daa + ml + stm + foit)
total_credits6 = (cdlc + mllc + stmlc + csc + cdc + daac + mlc + stmc + foitc)
sgpa32 = total_point6/total_credits6

'''
        print(total_point6)
        print(total_credits6)
'''
print(colored('Sem 6 - SGPA : ','green'))
print(colored(sgpa32,'yellow'))
print()


