# TNA to TE calculator

To reader:
In summary, the program allows us to calculate from a given TNA (Annual Nominal Rate) to a TE (Effective Rate). 
As a little introduction: the TNA in finance can be related to an interest rate offered by banking institutions in which is specified an 'x' period where the payments will be realized.
On the other hand, the TE is the amount of interest we will actually obtain from the operation in the desired period x.

## Where we can find a TNA?

The TNA is given by banking institutions and is very common, for instance, if we want to realize operations like fixed deposits.

## Hypothetical case study
If we had a TNA (x) = 24%. Where x represents the period of time (suppose we have x = 30) at the end of the year, we will receive 24% for each monetary amount invested and for had being invested every 30 days for a time-lapse of a year. The main difference between a TE and a TNA, and I will talk about it in a second, is that the TNA is based on a simple interest concept, this means that the interest is not reinvested in each period.
Now if we think about the TE we assume that the amount earned per period is reinvested, so the results between TNA and TE will be different and, therefore, the TEA (efective annual rate) will always be greater than the TNA. 
Efective rates are tied on a compound interest basis rather than simple interest as I already mentioned above.

## How does the passage between effective interest rates work? 

Once we have the TE(x) (effective rate in a specific period of time), if we change the period we will have a different kind of return in our operation so, being said this, is not the same as a TE(30) that a TE(90) because in the first case we will have an interest reinvestment in a short period, with this, the money we use in the operation is retained by the financial institution for a less period in comparison with the TE(90) and of course this final interest rate will be bigger because the invested money will be retained for a longer period. In summary, the money perceived in x = 90 will be bigger and we will earn more interest per monetary unit but, on the other hand, we will have less liquidity and consequently less money available for that period of time. 

## Why did I implement the software?
The main aim of the Software is to make things easier when we, as investors, want to calculate a TNA without using a calculator or even if we don't have the resources to calculate the rates. So the main idea is to speed up the process. In parallel, this is a project to improve my Python skills as a newbie in the field.

## Observations about the program
*The program was made in Spanish.

*I tried to prevent some kind of common errors from the users as typing errors and so. Even so, I couldn't fix problems in which the input must a number so if it types a letter   where a number must be, the program will close automatically.

*There are some times in the program in which there is a second interest rate defined as TNAA. This rate is for discounted operations and has the same logic as the TNA but if     we want it to do the inverse operation. Instead of capitalized we are applying a discount operation. 

*The program is based 365 days a year. There are many ways to calculate the rates but I tried to keep it simple. 

# Enjoy the program!
Greetings

_Orlando Tiziana Andrea
