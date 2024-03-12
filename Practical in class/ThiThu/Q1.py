class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        inputf1 = inputString.split(', ')
        for x in inputf1:
            print(x)
        pass
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        inputf1 = inputString.split(', ')
        inputf2 = []
        for x in inputf1:
            inputf2.append(int(x.split()[1]))
        up, down, left, right = [x for x in inputf2]
        distance = ((up-down)**2 + (left-right)**2)**(1/2)
        
        print(round(distance))

        pass
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

