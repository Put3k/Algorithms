# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).

# For example:

# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}

# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.

# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.
import unittest

def parse_molecule (formula):
    def slice_string_in_brackets(string, current_i):
        brackets = {"[": "]", "(": ")", "{": "}"}
        if string[current_i] in brackets:
            temp_string = string[current_i:]
            l_str_len = len(string[:current_i])
            temp_br_i = temp_string.find(brackets[string[current_i]])
            end_br_i = l_str_len + temp_br_i
        
        # Check if there is index after bracket
        if end_br_i != len(string)-1 and string[end_br_i + 1].isnumeric():
            n_multiplier = int(string[end_br_i + 1])
        else:
            n_multiplier = 1
        
        # Slice new string to recusrive func.abs
        sliced_str = string[current_i+1:end_br_i]

        return sliced_str, n_multiplier

    def get_index(index_holder, multiplier):
        if index_holder:
            index = int(index_holder) * multiplier
        else:
            index = 1 * multiplier
        return index

    def parsing(string, mol_dict, multiplier=1):
        atom=""
        index_holder = ""
        index=1 * multiplier
        skips = 0

        for i, char in enumerate(string):
            #perform skips
            if skips:
                skips -= 1
                continue

            # New Handle numbers
            if char.isnumeric():
                index_holder += char
                if i == len(string) - 1:
                    if not atom:
                        index_holder = ""
                        continue
                    index = get_index(index_holder, multiplier)
                    mol_dict[atom] = mol_dict.get(atom, 0) + index
                    index_holder = ""
                if not atom:
                    index_holder = ""
                continue
            
            # Handle letters
            if char.isalpha():
                # Uppercase
                if char.isupper():
                    if not atom:
                        atom += char
                        if i == len(string) - 1:
                            index = get_index(index_holder, multiplier)
                            mol_dict[atom] = mol_dict.get(atom, 0) + index
                            index_holder = ""
                        continue
                    else:
                        index = get_index(index_holder, multiplier)
                        mol_dict[atom] = mol_dict.get(atom, 0) + index
                        index_holder = ""
                        atom = char
                        index = 1 * multiplier
                        if i == len(string) - 1:
                            index = get_index(index_holder, multiplier)
                            mol_dict[atom] = mol_dict.get(atom, 0) + index
                            index_holder = ""
                        continue
                        
                # Lowercase
                if char.islower():
                    if atom[-1].isupper():
                        atom += char
                        if i == len(string) - 1:
                            index = get_index(index_holder, multiplier)
                            mol_dict[atom] = mol_dict.get(atom, 0) + index
                            index_holder = ""
                        continue
                    else:
                        raise ValueError("ATOM CANNOT START WITH LOWER CASE!")
                    
            # Brackets
            if char in ["[", "(", "{"]:
                if atom:
                    index = get_index(index_holder, multiplier)
                    mol_dict[atom] = mol_dict.get(atom, 0) + index
                    index_holder = ""
                    atom = ""
                    index = 1*multiplier
                new_string, n_multiplier = slice_string_in_brackets(string, i)
                skips += len(new_string) + 1
                parsing(string=new_string, mol_dict=mol_dict, multiplier=multiplier*n_multiplier)

    mol_dict={}
    parsing(string=formula, mol_dict=mol_dict)
    return mol_dict


formula = "{[Co(NH3)4(OH)2]3Co}(SO4)3"
print(parse_molecule(formula))