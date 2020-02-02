# Problem Set 4A
# Name: Alec Dewulf
# Collaborators: N/A
# Time Spent: 1:00

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = []
    
    # base case
    if len(sequence) == 1:
        return [sequence]
    
    # recursive solution to strings of len greater than 1
    else:
        p = []
        last_let = sequence[-1]
        # create a new list "sequence" without the last letter
        sequence = sequence[:-1]

        # get the permutations of the sequence without the last letter
        prev_p = get_permutations(sequence)

        # permutations in previous smaller sequences
        for p in prev_p:
            # all the positions for a new letter to be placed in the sequence
            for pos in range(0, len(p)+1):
                # place the letter into that pos
                new_p = p[:pos] + last_let + p[pos:]
                # append the permutation
                perms.append(new_p)
        
        return list(perms)

# testing code
if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    

