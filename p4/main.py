# This line is a comment because it starts with a pound sign (#). That                                                                                                                                         
# means Python ignores it.  A comment is just for a human reading the                                                                                                                                          
# code.  This project involves 20 small problems to give you practice                                                                                                                                          
# with operators, types, and boolean logic.  We'll give you directions                                                                                                                                         
# (as comments) on what to do for each problem.                                                                                                                                                                
#                                                                                                                                                                                                              
# Before you get started, please tell us who you are, putting your
# Net ID and your partner's Net ID below (or none if your working solo)                                                                                                                                      
#
# project: p4
# submitter-netid: yzeng58
# partner-netid: none

def AskQuestion(question,truth,hint="Check the textbook",times=1):
    print(question)
    while (times>0):
        times = times - 1                  
        answer = input("Your answer: ")
        if str.lower(truth) != str.strip(str.lower(answer)):
            if (times == 0):
                print("You answered '%s'. The correct answer is '%s'." %(answer, truth))
            elif (times == 1):
                print(hint)
            print("You have this many remaining tries:",times)
        else:
            print("\nCongratulations! You got it right.")
            return True
    return False
        
    
iteration = int(input("How many tries do you want for each question: "))
times = iteration
q1 = "\nWhat is the type of the following? \"1.0\" + \"2.0\"\n a) int\n b) float\n c) str\n d) bool\n e) NoneType"
q2 = "\nWhat is the type of the following? \"1\" * 2"
q3 = "\nWhat does this expression evaluate to?\n True != (3 < 2)"
correct = 0
hint = "Check the textbook"
if AskQuestion(q1,'c',hint,times) == True:
    correct = correct + 1

times = iteration
hint = 'notice the quotes!'
if AskQuestion(q2,'str',hint,times) == True:
    correct = correct + 1
        
times = iteration
hint = "Calcuate the right side first. Don't forget != means not equal to."
if AskQuestion(q3,'True',hint,times) == True:
    correct = correct + 1

print("You tried 3 questions and got",correct,"right.\n")
