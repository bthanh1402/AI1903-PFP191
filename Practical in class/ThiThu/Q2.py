class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        import random
        a = 0
        b = int(number)
        while True:
            guessNum = random.randint(a,b)
            state = input('Is  ' + str(guessNum) + ' too high(h), too low(l), or correct(c): ')
            if state == 'l':
                a = guessNum + 1
            elif state == 'h':
                b = guessNum - 1
            elif state =='c':
                print('Welldone! The computer guessed your number',str(guessNum),'correctly!')
                return guessNum
            
        pass
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()

