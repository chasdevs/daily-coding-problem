

class Solution:
    
    def oddEvenJumps(self, A):
        n = len(A)
        print(list(range(n)))
        print(A)
        print(A[-1])
        print('-'*3*n)
        next_higher, next_lower = [0] * n, [0] * n

        print(sorted([a, i] for i, a in enumerate(A)))
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                p = stack.pop()
                print(f'setting next_higher[{p}]={i}')
                next_higher[p] = i
            print(f'stacking {i}')
            stack.append(i)
        print(next_higher)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
        

s = Solution()
arr = [2,3,1,1,4]
s.oddEvenJumps(arr)