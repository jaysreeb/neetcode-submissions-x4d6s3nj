class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string
        result = "" 
        for word in strs:
            # Convert the len to a string and then add everything together
            result += str(len(word)) + "#" + word
        return result
    #Strings are immutable , for every result+ , it creates brand new string in memory. So, space complexity will be O(n) and for time complexity O(n)-> For the Encode part 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j +1: j+1+length])

            i = j + 1 + length
        return result

# Time and space will be O(n)


