"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def extract_and_rearrange(string): #I have indented the def so it will work probely, and i add extract it was having a spiling mistake
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    str_2 = "".join(string[6:13].split('ro'))#i have fix the spiling mistake in split
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))#I have add the underscour in str_3
    str_4 = "".join(string[21:29].split(string[23:28]))

    return str_1 + " " + str_2 + " " + str_3 + " " +str_4# I have add the + next to str_4

def ultra_extrct_and_rearrange(string):# I have added the : after (string)
    first_transform = extract_and_rearrange(string)
    return first_transform

print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv"))#I have added the _ in and_rerramge and i deleted one " after forjmxv
                                 
#after i run the program i have seen this massege(The quick brown fox)