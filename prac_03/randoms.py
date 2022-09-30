"""
CP1404 2022 Prac 03
Erica Finlay

Walkthrough Example
Random Numbers
"""

# Question - What did you see on line 1?
# 9
# The smallest number could have been 5, and the largest could have been 20.
#
# Question - What did you see on line 2?
# 5
# The smallest number could have been 3, and the largest could have been 10.
# No, this could not have produced a 4 because the range of numbers goes up from 3 by 2's. eg 3, 5, 7, 9
#
# Question - What did you see on line 3?
# 3.5909401550520386
# The smallest number could have been 2.5, and the largest could have been 5.5.

import random

print(random.randint(1, 100))
