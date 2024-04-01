class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
         # Start from the end of the string and find the index of the first non-space character
        end_index = len(s) - 1
        while end_index >= 0 and s[end_index] == ' ':
            end_index -= 1
        # Does not loop because condtion is not met, so end stays at index 10

        # Find the beginning of the word (the index of the space before the word or -1 if the word is at the start)
        start_index = end_index
        while start_index >= 0 and s[start_index] != ' ':
            start_index -= 1

        # Return the length of the last word, which is the difference between the end and start indices
        # Add 1 because end_index is the last character of the last word and
        # start_index is the space before the last word (or -1 if the word is at the start)
        return end_index - start_index
