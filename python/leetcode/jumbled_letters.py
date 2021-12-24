'''

zero
one
two
three
four
five
six
seven
eight
nine

Unique counts:
0: z, ero
2: w, to
4: u, for
6: x, si
8: g, eiht

3: count(h) - count(8)
7: count(s) - count(6)

5: count(v) - count(7)
1: count(o) - count()



The number of 'z' in s is number of 0s. 
The number of 0 is number of 'z'
The number of 3 is number of 'h' - count(8)



'''
class Solution:
    def originalDigits(self, s: str) -> str:
        zeros = s.count('z')
        twos = s.count('w')
        fours = s.count('u')
        sixes = s.count('x')
        eights = s.count('g')

        threes = s.count('h') - eights
        sevens = s.count('s') - sixes
        fives = s.count('v') - sevens

        ones = s.count('o') - twos - zeros - fours
        nines = s.count('i') - eights - sixes - fives

        return "0"*zeros + "1"*ones + "2" * twos + "3" * threes + "4" * fours + "5" * fives + "6" * sixes + "7" * sevens + "8" * eights + "9" * nines
    
s = Solution()
s.originalDigits("zeroonetwothreefourfivesixseveneightnine")