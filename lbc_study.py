import pandas


def xls_b26_to_b10(x):
    # TODO: check for anything other than [a-z]    
    zero_offset = 96        # make offset from ord('a') > 0
    col_num = -1            # automatically covert for 0 to 1 based
    b26 = 26                # 'a-z' is base 26
    
    # make lower and reverse order
    x = x.lower()[::-1]
    
    # get each value at each power of base 26
    b26_vals = [b26**(i)*(ord(j) - zero_offset) for i, j in enumerate(x)]
    
    # add base 26 power values to column number and return
    col_num += np.array(b26_vals).sum()
    
    return col_num

