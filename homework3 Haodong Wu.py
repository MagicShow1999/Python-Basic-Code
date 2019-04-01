#Part1

#1.
def judge_a_number():
    num = int(input("Enter a number:"))
    if num % 2 ==0 and num % 3 != 0:
        return True
    elif num % 2 != 0 and num % 3 ==0:
        return True
    else:
        return False
#2.
def judge_a_statement():
    statement = input("Choose a statement for evaluation:")
    answer1 = input("Is the statement True, False or Unknown according to experts in the relevant domain or according to some objective set of facts?")
    answer2 = input("Is the statement True, False or Unknown according to Donald Trump?")

    if answer1 == "True" and answer2 == "True":
        return "The statement is True"
    elif answer1 == "False" and answer2 == "False":
        return "The statement is False"
    elif answer1 == "Unknown" and answer2 =="Unknown":
        return "The statement is Unknown"
    elif answer1 == "False" or answer1 == "Unknown" and answer2 == "True":
        return "The statement is Alternative Fact"
    elif (answer1 == "True" or answer1 == "Unknown") and answer2 == "False":
        return "The statement is Alternative Falsehood"
    elif (answer1 == "True" or answer1 == "False") and answer2 == "Unknown":
        return "The statement is Alternative Unknown"
    else:
        return "Invalid input"
 
#Part2


#define the answer received from the player
def get_yes_or_no():

    
    while True:
        output= input("Please answer Yes or No.")
        if output =="Yes" or output== "yes":
            return(True)
            break
        elif output == "No" or output == "no":
            return(False)
            break
        else:
            print("Your answer is not clear, try again.")


intro = "A long time ago, there lives a princess called 'White Snow'. She is beautiful\
 and friendly to animals and people. Her stepmother is a vicious queen. Snow White lives happily\
 with her friends in the forest."

ending_1 = "A few days later Snow White was found dead beside a stream. It was said\
 the queen was jealous of her beauty so she just assigned a killer murdered her."

ending_2 = "Snow White was poisoned and lost her consciousness but finally was\
 rescued by a brave prince who kissed her and woke her up again. They lived happily since then. End of story!"



def story():
    print(intro)
    print("One day, she suddenly got tracked by a huntsman but was a little feared to\
 ask him what was wrong. Should she ask the huntsman what happened?")
    if get_yes_or_no() == True:
        print("The huntsman told her that the queen wanted her to die because she was so jealous\
 of White's beauty. Snow White was panicked and ran as fast as her can. Soon she found\
 a cottage in front of her. Should she enter it?")
        if get_yes_or_no() == True:
            print("There she found seven beds and messy clothes as well as uncleaned\
 dishes in the sink.She was so sleepy that she wanted to go to bed regardless of\
 the owner of the beds. Should she sleep on bed?")
            if get_yes_or_no() == True:
                print("Snow White was awaken by seven dwarfs who kept staring her\
 and seemed so confused. After she explained why she came here, she got great support\
 from the seven dwarfs and they provided her accommodation. Several days later, a peddler\
 woman gave Snow a red apple, saying it's nutritious and good for health. Should Snow take it?")
                if get_yes_or_no() == True:
                    print(ending_2)
                else:
                    print("You're so smart! The woman was actually the bad queen! However, when\
 Snow White refused the woman's request, the woman soon killed Snow by her knife.")

            else:
                print("She was so tired and exhausted and illusion came attacking her, finally drove her mad.")

        else:
            print("Night comes and the outside is so cold and freezing, she can't survive without warmth\
 Finally, she died outside the house. Although she was found by the owner of the house--seven dwarfs, she still\
 could not be saved alive.")
    else:
        print(ending_1)
    
story()
