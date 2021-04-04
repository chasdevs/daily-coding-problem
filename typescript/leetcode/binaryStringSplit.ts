/**
 * @param {string} s
 * @return {number}
 */
var numWays = function(s) {

    // 0012233456 // running count
    // 0123456789 // index
    // 0011010111 // string
    // C = 2

    // 112233
    // 012345
    // 101010
    // S = 3, p = 1
    // C = 4

    // 0000
    // 0123
    // 0000
    // (4 3)


    // s1 is at index 0, add all possible permutations of s3
    // s1 at index 1, add all possible permutations of s3
    // sum those to get result

    // what is computePermutations()?
    //  // start at the end of the running count and count inwards
    //  // count number of indices where value is 3*p

    // total number of ones is 6
    // s1 = s2 = s3 = 2 // s1 + s2 + s3 = 6

    // s1 can only be 0:4-5 (2)
    // s2 can only be 3-5:8 (4)
    // s3 can only be 8:9 (6)


    // edge cases:
    //   if total sum is not divisible by 3 (sum % 3 > 0)
    //   if answer super large return result % (10^9 + 7)

    // steps:
    // 1. build running count map
    // 2. check that total sum S is divisible by 3, if not return 0
    // 3. divide by 3 to get size S such that count_ones(s1) = p, count_ones(s2) = 2*p, ...
    // 4. iterate along running count
    //      for each possible s1 index, compute the number of possible s3 values
    //

    const n = s.length
    let v = 0;
    const runningCount = s
        .split('')
        .map((s: string) => {
            if (s == '1') {
                v++;
            }

            return v;
        })

    const S = runningCount.slice(-1)

    if (S%3 > 0) {
        return 0;
    }

    if (S == 0) {
        return (n-1) * (n-2) / 2 % (10^9+7)
    }

    const p = S/3;

    let res = 0;
    let i = 0;
    for (let x in runningCount) {
        console.log(x)
    }

    for (let c of runningCount) {
        if (c > p) break;
        if (c == p && i < runningCount.length - 2) {
            const runningCountRight = runningCount.slice(i+1)
            for (let rval of runningCountRight) {
                if (rval == 2*p) {
                    res++
                }
            }
        }
    }

    return res

};

numWays('0100101');
