thuemorseseq
============

Rough Implementation to generate Thue Morse Sequence Using Python

To learn more about Thue Morse Sequence go to http://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence

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
