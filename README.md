# newtons-method
This can solve any equation of the form ax^z+bx+c=0 where z is positive using [newton's method](https://en.wikipedia.org/wiki/Newtons_method)

PRs to make the input to python function process are more robust are very welcome, autograd can then be used for automatic differentation of the python function
## Copyright
Copyright © 2020  Rory Sharp All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If you have not received this, see <http://www.gnu.org/licenses/gpl-3.0.html>.

For a (non-legally binding) summary of the license go to https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)
## Example valid equation inputs
5x^2+2x-3  
5x^2-2x-3  
5x^2-2x+3  
-5x^2+2x-3  
0x^2+5x-100  
1x^2+0x-20  
## Example invalid euqation inputs
x^2+5x+2 - there must be an a term (at the moment!)  
1x^-1+5x+2 - no negative powers (at the moment!)  
1x^3+1x^2+2 - too many terms (at the moment!)  
