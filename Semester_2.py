from termcolor import colored
print(colored("Semester 2 :","blue"))

try: 
    aplg = float(input('ap lab Grades:'))
    aplc = float(input('ap lab credits:'))
    apl = aplg * aplc

    ppslg = float(input('pps lab Grades:'))
    ppslc = float(input('pps lab credits:'))
    ppsl = ppslg * ppslc

    esg = float(input('es Grades:'))
    esc = float(input('es cresits:'))
    es = esg * esc

    m2g = float(input('m2 Grades:'))
    m2c = float(input('m2 credits:'))
    m2 = m2g * m2c

    apg = float(input('ap Grades:'))
    apc = float(input('ap credits:'))
    ap = apg * apc
    
    egg = float(input('engineering graphics Grades:'))
    egc = float(input('engineering graphics credits:'))
    eg = egg * egc

    ppsg = float(input('pps Grades:'))
    ppsc = float(input('pps credits:'))
    pps = ppsg * ppsc

    total_point2 = (apl + ppsl + es + m2 + ap + eg + pps)
    total_credits2 = (aplc + ppslc + esc + m2c + apc + egc + ppsc)
    sgpa12 = total_point2/total_credits2

    '''
        print(total_point2)
        print(total_credits2)
    '''
    print(colored('Sem 2 - SGPA : ','green'))
    print(colored(sgpa12,'yellow'))
    print()
    
except KeyboardInterrupt:
    print(colored('[!!] Semester 2 Interrupted.','red'))   

