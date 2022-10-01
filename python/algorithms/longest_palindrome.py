# python3 note: version has to be superior than 3
"""given a string s, returns the longest palindrome in s

1)check for some constraints to "s"
2)check if the original string "s" is a palindrome
3)if "s" is not a palindrome two bucles are created

    1)  the first bucle will iterate over "s" length-1 while
        this number higuer than 1(cause words are minimum 2 length,otherwise they are letters)

    2)  the second bucle uses the number of the first 
        bucle to find this substring from left to right

    eg: "cbbd" 
      will form follow substrings -> 'cbb','bbd','cb','bb','bd'
      when a palindrome be finded it would break the script and print
      that a palindrome was finded and it'll concatenate the substring
"""


def check_constrints(s:str):
    """the following criteria is checked

    1) 1<= s.length <= 1000

    2) s consist of only digit and letters
    """
    #checks the length of the string
    assert len(s)>=1 and len(s)<=1000

    #checks if is alphaNumeric("ñ" is included)
    assert s.isalnum()


def reverse_s(s:str)->str:
    """receives a string and returns it reversed"""
    reversed_s = ''

    for letter in reversed(s):
        reversed_s += letter

    return reversed_s


def check_if_palindrome(s:str)->bool:
    """checks if the string received is a palindrome

    returns
    -------
    reversed_s:str
        returns de string if is a palindrome
    False:bool
        returns False if is not a palindrome
    """
    reversed_s = reverse_s(s)
    if s == reversed_s:
        return reversed_s
    else:
        return False


def find_longest_palindrome(s:str):
    """ given a string s, returns the longest palindrome in s

    1)  the first bucle will iterate over "s" length-1 while
        this number higuer than 1(cause words are minimum 2 length,otherwise they are letters)

    2)  the second bucle uses the number of the first 
        bucle to find this substring from left to right

    eg: "cbbd" 
      will form follow substrings -> 'cbb','bbd','cb','bb','bd'
      when a palindrome be finded it would break the script and print
    """
    original_length = len(s)
    #bucle 1 sobre la longitud del substring en order descendente
    for l in range(original_length-1,1,-1):
        ind_1=0
        ind_2=l
        #bucle 2 hace un tipo de permutacion sobre los subtrings con longitud ind_2
        while ind_2 <= original_length:
            s_substring = s[ ind_1:ind_2 ]
            palindrome_finded = check_if_palindrome(s_substring)
            if palindrome_finded:
                print(f"palindromo encontrado:{palindrome_finded}")
                quit()
            ind_1=ind_1+1
            ind_2=ind_2+1


#punto de entrada, aqui empieza la ejecución
if __name__ == "__main__":
    """given a string s, returns the longest palindrome in s"""

    #this is the string, it could be changed here
    s = "babad" 

    #revisa algunas restricciones para "s" NOTESE QUE SI ALGUNA RESTRICCION ES DETECTADA UN AssertionError SERÁ IMPRIMIDO Y EL SCRIPT SE DETENDRÁ
    check_constrints(s)

    #revisa si "s" es un palindromo
    palindrome_finded = check_if_palindrome(s)
    if palindrome_finded:
        print(f"la palabra original es un palindromo: {palindrome_finded}")

    #si la palabra original no es palindromo entonces empieza a buscar en substrings de s
    else:
        find_longest_palindrome(s)

    #si no encuentra ningún palindromo lo notificará
    print("ningun palindromo se encontra entre las subcadenas de s ")
