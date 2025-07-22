"""
write a program to identify the type of ai(narrow,general,super) based on input 

"""
while True:

    description=input("Describe the ai system: ").lower()

if "specific task" in description or "one task" in description:
    print("this is a narrow ai(ANI)")
elif "multi task" in description or "human like" in description:
    print("this is a general ai(AGI)")
elif "superior to human" in description :
    print("this is a super ai(ASI)") 
else:
    print("type of ai could not be determined")