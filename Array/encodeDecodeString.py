"""
This is a premium leetcode question so solving in Lintcode - https://www.lintcode.com/problem/659/

Difficulty: Medium

Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

Solution
---------------
We may use an array to store each word char length, but catch is "we are not suppose to use extra memory".
So we prepend the string len along with a delimiter (becuase if a word contain other digit the lenght we assume to be will be an error.).
Eg: ["hi", "himesh"]

Here we use delimiter b/w length and string as "#"

Encode: 2#hi5#himesh
Decode: ["hi", "himesh"], with analyse the number in begining as len and exclude the delimiter

Edge cases
----------------
1) Charectors are not limited to a-z or 0-9. We need to identify which delimiter should we use in between each array items to form a single string.
2) The time complexity for encode and decode should be O(N), N is total chars.
3) Encode - We prepend length of string and here we use delimiter b/w length and string as "#"
4) Decode - exclude until the delimiter by traverse until #, since len can be a number of any digits

"""

class Solution:

    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        encodeStr = ""
        for string in strs:
            encodeStr += str(len(string)) + "#" + string

        return encodeStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decodeArray = []

        index = 0
        while index < len(str):
            lengthStr = ""
            # exclude until the delimiter, since len can be a number of any digits
            while str[index] != "#":
                lengthStr += str[index]
                index += 1
            
            lengthStr = int(lengthStr)
            decodeArray.append(str[index+1: index+lengthStr+1])
            index += lengthStr+1

        return decodeArray


solution = Solution()
print(solution.encode(["lint","code","love","you"]))
print(solution.decode(solution.encode(["lint","code","love","you"])))

print(solution.encode(["we", "say", ":", "yes"]))
print(solution.decode(solution.encode(["we", "say", ":", "yes"])))