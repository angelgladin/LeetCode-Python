# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        def ones_n(n):
            f = {
                1 : 'One',
                2 : 'Two',
                3 : 'Three',
                4 : 'Four',
                5 : 'Five',
                6 : 'Six',
                7 : 'Seven',
                8 : 'Eight',
                9 : 'Nine'
            }
            return f[n]
        
        def tens_less_twenty_n(n):
            f = {
                10 : 'Ten',
                11 : 'Eleven',
                12 : 'Twelve',
                13 : 'Thirteen',
                14 : 'Fourteen',
                15 : 'Fifteen',
                16 : 'Sixteen',
                17 : 'Seventeen',
                18 : 'Eighteen',
                19 : 'Nineteen'
            }
            return f[n]
        
        def tens_n(n):
            f = {
                2 : 'Twenty',
                3 : 'Thirty',
                4 : 'Forty',
                5 : 'Fifty',
                6 : 'Sixty',
                7 : 'Seventy',
                8 : 'Eighty',
                9 : 'Ninety'
            }
            return f[n]
        
        def tens(n):
            if n == 0:
                return ''
            if n < 10:
                return ones_n(n)
            elif n > 9 and n < 20:
                return tens_less_twenty_n(n)
            else:
                aux_tens = n // 10
                rest = n % 10
                return tens_n(aux_tens) + ('' if rest == 0 else ' ' + ones_n(rest))
        
        def hundreds(n):
            if n == 0:
                return ''
            s = ''
            aux_hundreds = n // 100
            if aux_hundreds != 0:
                s += ones_n(aux_hundreds) + ' Hundred'
            tens_aux = n - (aux_hundreds * 100)
            if tens_aux != 0:
                s += ' ' if aux_hundreds != 0 else ''
                s += tens(tens_aux)
            return s
        
        n = num
        billion = n // int(1e9)
        million = (n - (billion * int(1e9))) // int(1e6)
        thousand = (n - (billion * int(1e9)) - (million * int(1e6))) // int(1e3)
        rest =  n - (billion * int(1e9)) - (million * int(1e6)) - (thousand * int(1e3))
        
        s = ''
        if billion != 0:
            s += hundreds(billion) + ' Billion'
        if million != 0:
            s += ' ' if s else ''
            s += hundreds(million) + ' Million'
        if thousand != 0:
            s += ' ' if s else ''
            s += hundreds(thousand) + ' Thousand'
        if rest != 0:
            s += ' ' if s else ''
            s += hundreds(rest)
        return 'Zero' if n == 0 else s
