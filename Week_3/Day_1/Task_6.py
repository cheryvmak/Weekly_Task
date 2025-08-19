# create a user input to enter age 
age = int(input("Enter your age: "))

# create a user input to enter the utme score
score = int(input("Enter your UTME Score: "))

# minimum of 200 to be eligible
utme = (score >= 200)

# create a user input to enter yes or no for the choice choosen
sch_chosen = input("choose UNILAG as first choice(Yes or NO): ").title()

# create a user input to enter yes or no for meeting olevel requirements
o_level = input("Do you five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics(Yes or No)?: ").title()

# create a user input to enter yes or no for the post utme eligibility
p_utme = input("Are you eligible to participate in the university's online Post-UTME screening(Yes or No)?: ").title()

# use logical operators to determine the departmental cut-off marks
dept_cut_off = (score >= 200) and (score <= 320)

# this is criteria to offer admission using assignment operator
final_Ad = (age >= 16) and (utme == dept_cut_off)
#print("Admission status:", final_Ad)

# this is to map the admission status
Admission_status = {True: "Admission offered", False: "Not Admitted"}
print("Admission status:", Admission_status[final_Ad])