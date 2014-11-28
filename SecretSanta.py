from random import shuffle

def collect_users():
    list_of_santas = []
    
    while 1:
        item = input("Enter a name\n")
        if not item:
            break
        list_of_santas.append(item)

    return list_of_santas


def set_exceptions(list_of_santas):
    print("Please set any matchup exclusions\n")

    exception_dict = {}
    for name in list_of_santas:
        exception_dict[name] = []

    
    for name in list_of_santas:
        exception_dict[name] = ['name']
        #print("%s may not draw: %s" % name, exception_dict[name].join(" "))
        print("Who can %s not draw?" %name)
        name_in = input()
        while 1:
            if name_in == "":
                break
            if name_in not in list_of_santas or name_in == name:
                print("Please enter a valid name;\n They must be a santa, and cannot exclude themself")
            else:
                 exception_dict[name].append(name_in)
                 print("Who else can %s not draw?" %name)
            name_in = input()

    return exception_dict

def generate_matchups(exception_dict, list_of_santas):
    list1 = list(list_of_santas)
    list2 = list(list_of_santas)
    shuffle(list1)
    shuffle(list2)

    a = list(zip(list1,list2))
    b = []
    for entry in a:
        b.append(list(entry))
    return b

def test_matchup(matchup,exception_dict):
    for i in range(len(exception_dict)):
        print(matchup[i][0] + "->" + matchup[i][1])
        if matchup[i][1] in exception_dict[matchup[i][0]]:
            return False
    return True


d = {'krish':['sav','krish'],'sav':['krish','sav'],'gabs':['seb','krish','gabs'],'seb':['gabs','seb'],'tim':['tim']}


valid = False
while not valid:
    matchup = generate_matchups(d,"krish sav gabs seb tim".split(" "))
    print(matchup)
    valid = test_matchup(matchup,d)


print("done")
