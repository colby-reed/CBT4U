# CBT4U - Written by R. Colby Reed - Copywrite Apr. 11, 2024.
# This application walks you through Dr. David Burn's Triple Column Technique to help identify distorted thoughts,
# and replace them with more rational responses.  It also helps you identify the top distortions that leave you prone
# to depressive episodes.  It is not meant to be a substitute for a medical professional or medication.  Always
# consult your doctor regarding your condition and any resources you use, including this application.
# Licensed under GNU and free to use.
print("#######" + "#########" + "############" + "########" + "##########")
print("#######" + "   ########" + "  ########" + "##    ##" + "  ##    ##")
print("##" + "        ##    ##" + "     ##   " + "##    ##" + "  ##    ##")
print("##" + "        ########" + "     ##   " + "########" + "  ##    ##")
print("##" + "        ##    ##" + "     ##   " + "      ##" + "  ##    ##")
print("#######" + "   ########" + "     ##   " + "      ##" + "  ########")
print("#########" + "#######" + "############" + "########" + "##########")
print("")
print("")
done = str(input("Would you like to continue? Please type N to quit or press Enter to continue..."))
finished = str("N")
lower_finished = str("n")
while done != str(finished) and done != str(lower_finished):
    try:
        print("")
        print("List of Top 10 Cognitive Distortions")
        print("")
        distortions = [
            "All-or-Nothing Thinking - This refers to when you may evaluate yourself or others in extreme, black and white ways.",
            "Overgeneralization - This occurs when you see a single negative event as a never-ending pattern.",
            "Mental Filtering - This refers to a tendency to dwell exclusively on a single negative event, and thus perceive the whole situation as negative.",
            "Disqualifying the Positive - This is when you take neutral or positive experiences and turn them into negative ones.",
            "Jumping to Conclusions - This occurs when you jump to negative conclusions that are not justified by the facts of the situation.",
            "Magnification and Minification - In magnification, you are exaggerating the importance of a negative event or mistake.  If, for example, you experience a flare-up in your pain, you find yourself saying, I can’t stand this!  I can’t take this anymore!  As a matter of fact, however, you CAN!  In minification, conversely, you take positive personal qualities or events, and deny them of their importance.  For example, at a family gathering someone shares how great it is to see you, but you may think, A lot of good THAT does me, as I can’t participate in the family activities.",
            "Emotional Reasoning - This refers to when you use your emotions as evidence for truth.  If you feel something is right, then it must be true.  For instance, you find yourself thinking, I feel useless, THEREFORE I AM useless.",
            "Labeling - This is when you identify a negative quality or a mistake, and then describe an entire situation or individual in terms of that quality.",
            "Personalization – This describes when you take responsibility for a negative event, even when the circumstances are beyond your control.",
            "Should Statements – These are attempts to motivate by saying such things like, I should know better, I should go there, or I must do that."]
        len(distortions)
        for index in range(len(distortions)):
            print(distortions[index])
        print("")
        auto_thought = str(input("What was your automatic or negative thought? "))
        print("")
        print(auto_thought)
        print("")
    except int as err:
        print(err)
    except ValueError:
        print("Invalid input")
    # Use specific except functions...generic except is too broad.
    try:
        auto_thought = str(input("What cognitive distortions are present? "))
        print("")
        print(auto_thought)
        print("")
    except int as err:
        print(err)
    except ValueError:
        print("Invalid input")
    try:
        auto_thought = str(input("What is a more healthy, objective thought? "))
        print("")
        print(auto_thought)
        print("")
        print("Well Done!")
        print("")
        done = str(input("Would you like to continue? Please type N to quit or press Enter to continue..."))
    except int as err:
        print(err)
    except ValueError:
        print("Invalid input")





