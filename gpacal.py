import Semester_1
import Semester_2
import Semester_3
import Semester_4
import Semester_5
import Semester_6
import Semester_7

from termcolor import colored

''' 
    -- total grades = sum of all semester grades
'''
#sem1 = Semester_1().sgpa11
#sem2 = Semester_2().sgpa12
#sem3 = Semester_3().sgpa21
#sem4 = Semester_4().sgpa22
#sem5 = Semester_5().sgpa31
#sem6 = Semester_6().sgpa32
#sem7 = Semester_7.sgpa41
tg = Semester_1.total_point1 + Semester_2.total_point2 + Semester_3.total_point3 + Semester_4.total_point4 + Semester_5.total_point5 + Semester_6.total_point6 + Semester_7.total_point7

#tc1 = total_credits1 + total_credits2
#tc2 = total_credits3 + total_credits4
#tc3 = total_credits5 + total_credits6
#tc4 = Semester_7.total_credits7
tc = Semester_1.total_credits1 + Semester_2.total_credits2 + Semester_3.total_credits3 + Semester_4.total_credits4 + Semester_5.total_credits5 + Semester_6.total_credits6 + Semester_7.total_credits7

#sgpa = sem1 + sem2 + sem3 + sem4 + sem5 + sem6 + sem7
#tc = tc1 + tc2 + tc3 + tc4

#cgpa = float(sgpa/tc)
cgpa = float(tg/tc)
overall_percentage = float((cgpa - 0.5)*10)

print(colored('CGPA : ','red'))
print(colored(cgpa,'yellow'))
print(colored('Percentage: ','red'))
print(colored(overall_percentage,'magenta'))
