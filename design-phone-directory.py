# 379. Design Phone Directory
# https://leetcode.com/problems/design-phone-directory/

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.occupied_numbers = set()
        self.not_occupied_numbers = { x for x in range(maxNumbers) }
        

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        number = -1
        for x in self.not_occupied_numbers:
            number = x
        if number != -1:
            self.occupied_numbers.add(number)
            self.not_occupied_numbers.remove(number)
        return number
        

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.not_occupied_numbers
        

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.occupied_numbers:
            self.occupied_numbers.remove(number)
            self.not_occupied_numbers.add(number)
