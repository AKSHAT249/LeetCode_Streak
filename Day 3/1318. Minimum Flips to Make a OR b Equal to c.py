class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        def Decimal_To_Binary(num):
            binary = ""
            while num:
                binary+=str(num%2)
                num=num//2
            return binary[::-1]
        # print(Decimal_To_Binary(a))
        # print(Decimal_To_Binary(b))
        # print(Decimal_To_Binary(c))

        a_bin = Decimal_To_Binary(a)
        b_bin = Decimal_To_Binary(b)
        c_bin = Decimal_To_Binary(c)

        length = max(len(a_bin), len(b_bin), len(c_bin))

        if len(a_bin)<length:
            a_bin = (length-len(a_bin))*"0" + a_bin

        if len(b_bin)<length:
            b_bin = (length-len(b_bin))*"0" + b_bin

        if len(c_bin)<length:
            c_bin = (length-len(c_bin))*"0" + c_bin

        

        

        count = 0
        for i in range(len(a_bin)-1,-1,-1):
            if c_bin[i]=="0":
                if a_bin[i]=="1":
                    count+=1
                if b_bin[i]=="1":
                    count+=1
            else:
                if a_bin[i]=="0" and b_bin[i]=="0":
                    count+=1
        return count

