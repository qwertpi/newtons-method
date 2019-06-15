# newtons-method
This can solve any equation of the form ax^z+bx+c=0 where z is positive using [newton's method](https://en.wikipedia.org/wiki/Newtons_method)

PRs to make the input to python function process are more robust are very welcome, autograd can then be used for automatic differentation of the python function
## Example valid equation inputs
5x^2+2x-3
5x^2-2x-3
5x^2-2x+3
-5x^2+2x-3
0x^2+5x-100
1x^2+0x-20
## Example invalid euqation inputs
x^2+5x+2 - there must be an a term (yet!)
1x^-1+5x+2 - no negative powers (yet!)
1x^3+1x^2+2 - too many terms (at the moment!)
