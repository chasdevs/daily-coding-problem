class Solution:
    def stop(self):
        raise StopIteration()

    def myAtoi(self, s: str) -> int:
        # read in, ignoring leading whitespace
        # - left-trim whitespace

        # if not at the end, check if the next char is +/-, assume +

        INTEGERS = list(map(lambda i: str(i), range(0, 10)))

        stripped = s.lstrip()
        if len(stripped) < 1: return 0

        firstChar = stripped[0]

        positive = True
        if firstChar == '+':
            stripped = stripped[1:]
        elif firstChar == '-':
            positive = False
            stripped = stripped[1:]

        cleaned = ''
        for c in stripped.lstrip('0'):
            if (c not in INTEGERS): break
            cleaned += c

        if len(cleaned) < 1: return 0

        integer = int(cleaned)
        integer = integer if positive else -integer

        [low, high] = [pow(-2, 31), pow(2, 31) - 1]

        if integer > high: integer = high
        elif integer < low: integer = low

        return integer


(Solution()).myAtoi(" +000059203758237589327896d")