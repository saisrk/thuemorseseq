#!/usr/bin/env python

"""
This is a rough solution to generate Thue-Morse Sequence in Python.
Thue -Morse sequence is an infinite sequence of binary digits 0s and 1s.
The sequence starts with a 0 and next set of digits are the negated version
of the old set. It will be clear with example below.

--> 0  --> start
    1  --> negation
    01 --> new sequence
     
--> 01 --> old set
    10 --> negation
    0110 --> new set
    
--> 0110 --> old set
    1001 --> negation
    01101001 --> new set

We see that the new sequence length multiplies by power of 2.

Solution
========
There can be a better solution than this,
But regarding the below solution, 
Here the number of sets is controlled to get a finite sequence and
sequence is computed and printed at a stretch rather than one by one.

The same solution can be achieved in any format we want. 

1. It can be each digits printed one after the other with space. Ex: 0 1 1 0 1 0 0 1
2. Each digit printed one below the other.
Ex: 0
    1
    1
    0....
etc.

I have left out a abstract method format_output() which can be used to do it. :)
"""

import sys

def change(digit):
    """This method will change the digit from 0 to 1
    @param digit: It will be 0 or 1 which needs to be changed
    @return: The negated digit is returned
    """
    if digit == 1:
        return str(0)
    else:
        return str(1)
    
def negate(seq):
    """This method gets the entire sequence to be negated
    @param seq: The sequence of 0s and 1s which needs to be negated
    @return strseq: The neagted sequence of seq is returned
    """
    strseq = ''
    for edigit in seq:
        strseq = strseq+change(int(edigit))
    return strseq
    
def gen_thmorse_seq(noofsets):
    """This method is going to generate the thue-morse sequence
    @param noofsets: The control variable making the sequence finite.
    @return: prints out the data and does not return anything.                 
    """
    oseq = '0'
    while noofsets > 0:
        nseq = negate(oseq)
        noofsets = noofsets - 1
        lseq = oseq + nseq
        oseq = lseq
    print "The Thue Morse Sequence is : %s " % lseq

def format_output(output):
    """This method can be used to format the output based on requirement
    @param output: generated string output from gen_thmorse_seq()
    """
    # Feel free to format the same
    
         
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        gen_thmorse_seq(int(sys.argv[1]))
    else:
        print "Input for noofsets is not given"
