"""
Problem prompt:

Suppose that a scientist is doing some important research work that requires her to use rabbits 
in her experiments. She starts out with one pair of adult rabbits (a male and a female). At the
end of each month, a pair of rabbits produces one pair of offspring (a male and a female). 
However, these new offspring will not be able to reproduce until they are a month old, and won't
have babies of their own until the following month. To illustrate this, consider the first two months:

At the beginning of month one, the scientist just has the original 
one pair of adult rabbits. The table for month one will look something like

Month	Adult	Babies	Total
1	    1	    0	      1
 
At the end of month one this pair of adults produces one pair of offspring. Thus, at the 
beginning of month two the table will look like this:

Month	Adult	Babies	Total
1	    1	    0	      1
2	    1	    1	      2
 
At the end of month two the adults have another pair of baby rabbits. The first pair of 
babies, born at the end of last month are not old enough to have babies yet, but we will 
categorize them as adults. So, at the beginning of month three the table looks like this:

Month	Adult	Babies	Total
1	    1	    0	      1
2	    1	    1	      2
3	    2	    1	      3
 
The scientist has 500 cages in which to hold her rabbits. Each cage holds one pair of rabbits.
Assuming that no rabbits ever die, when will she run out of cages?

Your program must do the following:

1. Print a table that contains the following information for the beginning of each month.
2. The number of months that have passed.
3. The number adult rabbit pairs (those over 1 month old).
4. The number of baby rabbits pairs produced this month.
5. The total number of rabbit pairs in the lab.
6. Calculate how many months it will take until the number of rabbits exceeds the number of available cages.
7. Stop printing when you run out of cages.
8. Print a message giving how many months it will take to run out of cages
"""

def main():
    """
    Prints the months, adults, babies, and total number of rabbits produced from a pair of rabbits.
    Population growth pattern follows the Fibonacci sequence. Information is displayed in a 
    table format.
    """

    #Instantiates values for the current number of months, adults, youngadults, babies, and maxcages.
    months = 1
    adults = 1
    youngadults = 0
    babies = 0
    maxcages = 500

    #Calculates the total rabbits
    total = adults + youngadults + babies

    #Prints the heading for the table
    print ("Months", '\t', "Adults", "Babies", '\t', "Total")

    #Prints first line of table with initial values.
    print (months, '\t', adults, '\t', babies, '\t', total)

    #Prints each of the rows in the table and increments the months, adults, and babies
    #each time a month goes by. Loop stops when the total becomes more than the 
    #number of available cages.
    while total < maxcages:
        months += 1
        youngadults = babies
        babies = adults
        adults += youngadults
        total = adults + babies
        print (months, '\t', adults, '\t', babies, '\t', total)

    print("The scientist will run out of cages during month: ", months)
