from random import shuffle
import re

def collect_users():
    """Collect a list of all Santas from the user"""
    list_of_santas = []
    
    while 1:
        item = input("Enter a name\n")
        if not item:
            break
        list_of_santas.append(item)

    return list_of_santas


def set_exceptions(list_of_santas):
    """Set up any gifting exclusions that may exist"""
    print("Please set any matchup exclusions\n")

    #dict comprehension here would be more pythonic
    exception_dict = {}
    for name in list_of_santas:
        exception_dict[name] = []

    
    for name in list_of_santas:
        exception_dict[name] = [name]
        print("Who can %s not draw?" %name)
        name_in = input()
        while 1:
            if name_in == "":
                break
            if name_in not in list_of_santas or name_in == name:
                print("Please enter a valid name;\nThey must be a Santa, and cannot be themself")
            else:
                 exception_dict[name].append(name_in)
                 print("Who else can %s not draw?" %name)
            name_in = input()

    return exception_dict

def generate_matchups(exception_dict, list_of_santas):
    """pseudorandomly assign giftees to gifters"""
    list1 = list(list_of_santas)
    list2 = list(list_of_santas)
    shuffle(list1)

    #this is inelegant
    a = list(zip(list1,list2))
    b = []
    for entry in a:
        b.append(list(entry))
    return b

def test_matchup(matchup,exception_dict):
    """Test the proposed matchups agains the disallowed paths"""
	#TODO check for infinite loops - impossible solutions!!!!
    for i in range(len(exception_dict)):
        print(matchup[i][0] + "->" + matchup[i][1])
        #if giftee is in gifters list of exceptions:
        if matchup[i][1] in exception_dict[matchup[i][0]]:
            return False
    return True

def collect_email_addresses(list_of_santas):
	email_addresses = {}
	for name in list_of_santas:
		print("Please enter %s's email address"%name)
		while 1:
			email_addy = str(input())
			if not re.match(r"[^@]+@[^@]+\.[^@]+", email_addy):		#regex for [chars]@[chars].[chars]
				print("Please enter a valid email address")
			else:
				email_is_correct = input("%s - is this correct? (y/n)" % email_addy)
				if email_is_correct.lower() == 'yes' or email_is_correct.lower() == 'y':
					email_addresses[name] = email_addy
					break
				else:
					print("Please re-enter the email address")
	return email_addresses

	
#d is a test dictionary - collect_users and set_exceptions works, this is to speed up testing
#d = {'krish':['sav','krish'],'sav':['krish','sav'],'gabs':['seb','krish','gabs'],'seb':['gabs','seb'],'tim':['tim']}

#######
#this is a loop that could be used in the final program?
#naively generate matchups until one is found that does not break the rules?

users = collect_users()
emails = collect_email_addresses(users)
print(emails)
exceptions = set_exceptions(users)
valid = False
counter = 0
while not valid:
	counter +=1
	matchup = generate_matchups(exceptions,users)
	print(matchup)
	valid = test_matchup(matchup,exceptions)
#end of potential real code
######

print("done")
print("took %d iterations" % counter)
