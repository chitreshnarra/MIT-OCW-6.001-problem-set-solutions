import string
    def build_shift_dict(shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict = {}
        lower_case = list(string.ascii_lowercase)
        upper_case = list(string.ascii_uppercase)
        for i in range(26-shift):
            shift_dict[lower_case[i]] = shift_dict.get(lower_case[i],'')+lower_case[i+shift]
        for i in range(26-shift,26):
            shift_dict[lower_case[i]] = shift_dict.get(lower_case[i],'') + lower_case[i-(26-shift)]
        for i in range(26-shift):
            shift_dict[upper_case[i]] = shift_dict.get(upper_case[i],'')+upper_case[i+shift]
        for i in range(26-shift,26):
            shift_dict[upper_case[i]] = shift_dict.get(upper_case[i],'') + upper_case[i-(26-shift)]
        return shift_dict
        
    def apply_shift(message, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        message_text = ''
        shift_dict = build_shift_dict(shift)
        for x in message:
            if x in shift_dict.keys():
                message_text += shift_dict[x]
            else :
                message_text += x
        return message_text

print(build_shift_dict(7))
print(apply_shift('deku',7))