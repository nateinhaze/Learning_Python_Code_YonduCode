# Learning_Python_Code_YonduCode
Problem

Yondu Udonta and his crew of space pirates arrive at the Iron Lotus after several weeks of plundering the high seas. Since the crew has been in space for nearly six months, they are ready for a night of celebration. Yondu doesn’t want to divvy up the plunder just yet, so he gives each crew member other than himself and Peter Quill 3 units and sends them off to the Iron Lotus. (We’re keeping the units simple for purposes of the problem, even though 1 unit is about $2.33.) After the crew has gone, he and Peter count what’s left and decide how to split it up among the crew. Yondu takes 13% plunder, which he transfers to a hidden bank account. Yondu gives Peter 11% of the remaining units, which Peter transfers to his account. The next morning, the remaining units are divided evenly among all of the crew, including Yondu and Quill. Little do they know that Yondu and Quill have already taken a cut. If the remaining treasure can’t be split evenly, the units left over are given to the Reaver’s Benevolent Fund (RBF).
The problem is to compute how many units each person gets and how how much goes to the RBF. A unit cannot be split, so if some calculation yields a number that contains a fractional part, you can only give that person the integer part of the value. For example, if your program computed the captain’s share as 25.67 units, you could only give him 25 units, not 25.67 units. Warning: Always round down, NOT up. Simply drop the fractional part, but don’t lose any units from the overall total amount.
