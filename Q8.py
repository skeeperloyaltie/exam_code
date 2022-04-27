# Assume that we are spies working for the spy organization United Network Command for
# Law and Enforcement (UNCLE) and we need to pass messages back and forth without 
# others being able to read them directly.

# We come up with a code by which we can transform any given message into a 
# code which has the form of: digit, followed by a string in square brackets.  
# Within that string, there may be another digit and string in square brackets.  
# Each digit corresponds to a multiplier of the string inside the brackets.  
# In order to recreate the original message, you need to evaluate the code from 
# the interior set of brackets out.  You can assume the code always starts with with
# a digit and that nothing ever follow a closing bracket other than balancing closing 
# brackets.

# You are to create a function called decode(code) where the parameter is the 
# input code of the form described above, and return the decoded message.  

# In order to help you, a function called find_first_digit(s) is available and does 
# not need to be imported.  This method takes in a string s, and returns the index of 
# the first digit (0-9) in the string or -1 if there isn't one.  
# A reminder that there are also two functions standard string methods, 
# find and rfind, that allow you to search strings for particular values.

# For example:
# Test 	Result

# print(decode("2[a]"))
# aa

# print(decode("2[a3[b]]"))
# abbbabbb

# print(decode("3[ab2[cd]]"))
# abcdcdabcdcdabcdcd

def decode(code):
    if code[0] == "[":
        return decode(code[1:])
    elif code[0] == "]":
        return ""
    else:
        return code[0] + decode(code[1:])
    
def find_first_digit(s):
    if s[0] in "0123456789":
        return 0
    else:
        return find_first_digit(s[1:])
    
def main():
    print(decode("2[a]"))
    print(decode("2[a3[b]]"))
    print(decode("3[ab2[cd]]"))
    
if __name__ == "__main__":
    main()

