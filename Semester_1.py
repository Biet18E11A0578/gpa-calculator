from termcolor import colored
print(colored("Semester 1 :","blue"))

try:    
    wg = float(input('Engineering Workshop Grade:'))
    wc = float(input('Engineering workshop Credits:'))
    workshop = wg * wc

    clg = float(input('chemistry_lab Grade:'))
    clc = float(input('chemistry_lab Credits:'))
    chem_lab = clg * clc
    
    elg = float(input('elcs_lab Grade:'))
    elc = float(input('elcs_lab Credits:'))
    elcs_lab = elg * elc
    
    blg = float(input('bee_lab Grade:'))
    blc = float(input('bee_lab Credits:'))
    bee_lab  = blg * blc

    m1g = float(input('M1 Grades:'))
    m1c = float(input('M1 Credits:'))
    m1 = m1g * m1c

    cg = float(input('chemistry Grades:'))
    cc = float(input('chemistry credits:'))
    chem = cg * cc

    beeg = float(input('bee Grades:'))
    beec = float(input('bee credits:'))
    bee = beeg * beec

    englishg = float(input('english Grades:'))
    englishc = float(input('english credits:'))
    english = englishg * englishc

    total_point1 = (workshop + chem_lab + elcs_lab + bee_lab + m1 + chem + bee + english)
    total_credits1 = (wc + clc + elc + blc + m1c + cc +beec + englishc)
    sgpa11 = total_point1/total_credits1

    ''' print(total_point1)
        print(total_credits1)
    '''
    print(colored('Sem 1 - SGPA : ','green'))    
    print(colored(sgpa11,'yellow'))
    print()

except KeyboardInterrupt:
    print(colored('[!!] Semester 1 is Interrupted','red'))

