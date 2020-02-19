# 157. Read N Characters Given Read4
# https://leetcode.com/problems/read-n-characters-given-read4/

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # Pointer of the current position in `buf`
        idx = 0
        # Auxiliary array for storing the the characters read by read4
        tmp_buffer = ['']*4
        # While there are characters to read
        while n > 0:
            chars_read = read4(tmp_buffer)
            # read4 function has not read anything
            if chars_read == 0:
                return idx
            # Hold two cases, write the characters in buffer array or read up to n chars
            for i in range(min(chars_read, n)):
                buf[idx] = tmp_buffer[i]
                idx += 1
                n -= 1
        return idx
