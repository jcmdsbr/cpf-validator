# The CPF Validator  :sunglasses:

Basic learning concepts in python applied in  CPF algorithm

## Give a Star! :star:
If you liked the project, please give a star ;)

## You need some of the fallowing tools :exclamation:

- Visual Studio Code or PyCharm
- Python 2+

## Description :books:

- Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms. [Redirect to official documentation](https://docs.python.org/3/tutorial/index.html)

### CPF Algorithm :bulb:

The CPF validation algorithm calculates the first check digit from the first 9 digits of the CPF and then calculates the second check digit from the 9 (nine) first digits of the CPF, plus the first digit, entered in the first part.

- The first CPF check digit is appropriate using the following algorithm.
  - Distribute the first 9 digits on a board by placing the weights 10, 9, 8, 7, 6, 5, 4, 3, 2 below from left to right 
  - Multiply the values of each column
  - Calculate the sum of the results
  - The result obtained will be divided by 11. Consider as a quotient only the whole value, the rest of the division will be responsible for the calculation of the first check digit.If the rest of the division is less than 2, our first check digit becomes 0 (zero), otherwise the value obtained from 11 is subtracted, which is our case
- Calculating the Second Check Digit 
  - For the calculation of the second digit, the first check digit already calculated will be used. We will set up a table similar to the previous one, but this time we will use the values 11,10,9,8,7,6,5,4,3,2 in the second line since we are incorporating one more number for this calculation.
  - In the next step we will do as in the situation of calculating the first check digit, multiply the values of each column and make the sum of the results obtained
  - We again performed the calculation for module 11. We divided the sum total by 11 and considered the rest of the division.
  - If the value of the rest of the division is less than 2, this value automatically becomes zero, otherwise (as in our case) it is necessary to subtract the value obtained from 11 to obtain the check digit.
