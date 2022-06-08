from termcolor import colored
print(colored("Semester 3 :","blue"))

adelg = float(input('ade lab Grades:'))
adelc = float(input('ade lab credits:'))
adel = adelg * adelc

cpplg = float(input('c++ lab Grades:'))
cpplc = float(input('c++ lab credits:'))
cppl = cpplg * cpplc

dslg = float(input('data structures lab Grades:'))
dslc = float(input('data structures lab cresits:'))
dsl = dslg * dslc

itwg = float(input('IT workshop lab Grades:'))
itwc = float(input('IT workshop lab credits:'))
itw = itwg * itwc

gslg = float(input('gender sensitization lab Grades:'))
gslc = float(input('gender sensitization lab credits:'))
gsl = gslg * gslc

adeg = float(input('ade Grades:'))
adec = float(input('ade credits:'))
ade = adeg * adec

coag = float(input('coa Grades:'))
coac = float(input('coa credits:'))
coa = coag * coac

cosmg = float(input('cosm Grades:'))
cosmc = float(input('cosm credits:'))
cosm = cosmg * cosmc

dsg = float(input('data structures Grades:'))
dsc = float(input('data structures credits:'))
ds = dsg * dsc

cppg = float(input('c++ Grades:'))
cppc = float(input('c++ credits:'))
cpp = cppg * cppc


total_point3 = (adel + cppl + dsl + itw + gsl + ade + coa + cosm + ds + cpp)
total_credits3 = (adelc + cpplc + dslc + itwc + gslc + adec +coac + cosmc + dsc + cppc)
sgpa21 = total_point3/total_credits3

'''
    print(total_point3)
    print(total_credits3)
'''    
print(colored('Sem 3 - SGPA : ','green'))
print(colored(sgpa21,'yellow'))
print()

