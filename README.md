# palindrome

The 22nd of Feb 2022 was a "palindrome" date. I.e. the date "22 02 2022" is the same whether it's read forwards or backwards.

There is a maths procedure for generating palindrome numbers, as follows...

Let's pick a number: 174
The reverse order of 174 is 471.
Repeatedly add forward order to reverse order...
174 + 471 = 654 (1st)
654 + 456 = 1191 (2nd)
1191 + 1911 = 3102 (3rd)
3102 + 2013 = 5115 (4th)

5115 <--- is a palindrome number
In summary, commencing with 174, it then took 4 iterations to reach the palindrome number of 5115.

The python program [palindrome.py](palindrome.py) is for calculating palindrome numbers.

## Examples:

$ python palindrome.py
Start integer [100]: 174
Range integer [100]: 1
Display iterations from [0]:

   Integer Iter. Palindrome
       174     4 5115

OR... for a range of numbers from 186 to 200...

$ python palindrome.py
Start integer [100]: 186
Range integer [100]: 15
Display iterations from [0]:

   Integer Iter. Palindrome
       186     3 6996
       187    23 8813200023188
       188     7 233332
       189     2 1881
       190     7 45254
       191     0 191
       192     4 6996
       193     8 233332
       194     3 2992
       195     4 9339
       196   300 Not found
       197     7 881188
       198     5 79497
       199     3 3113
       200     1 202


Note that 196, after 300 iterations had not turned up a palindrome number.
To see which numbers in the first 1000 don't have palindrome numbers within 300 iterations...

$ python palindrome.py
Start integer [100]: 1
Range integer [100]: 1000
Display iterations from [0]: 300

   Integer Iter. Palindrome
       196   300 Not found
       295   300 Not found
       394   300 Not found
       493   300 Not found
       592   300 Not found
       689   300 Not found
       691   300 Not found
       788   300 Not found
       790   300 Not found
       879   300 Not found
       887   300 Not found
       978   300 Not found
       986   300 Not found

According to wikipedia, at 261 iterations, this is meant to be the largest number with a palindrome...

$ python palindrome.py
Start integer [100]: 1999291987030606810
Range integer [100]: 1
Display iterations from [0]:

   Integer Iter. Palindrome
1999291987030606810   261 44562665878976437622437848976653870388884783662598425855963436955852489526638748888307835667984873422673467987856626544
