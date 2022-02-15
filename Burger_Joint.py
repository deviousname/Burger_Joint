class Burger_Joint():    
    def __init__(self):
        self.e = ["quit", "back", "escape", "stop", "halt", "exit", "no", "bye"]
        self.h = ["help", "h", "?", "what", "how"]
        self.w = ["finish", "winner", "passed"]
        self.a = []
        self.q = False
        self.b = ["true", "false"]
        self.m = [self.e,self.h,self.w,self.a,self.q]
        self.l = 0
        # i + 0 = loop lock that it won't pass yet
        self.i()    # this is back forth loop
        self.o()    # that needs unlock to pass
        # i + 0 = loop lock that it won't pass yet
        print("Your adventure:")
        for i in self.a:
            print(i)            
        self.l += 1
        print (f'Score: {self.l}')
        print (self.m[0][-1])        
        self.i()        
    def i(self):
        self.m = self.m
        self.z = input("What? ")
        if self.z == self.e[0]:
            print("Don't give up!")
            self.q = True
            self.i()            
        elif self.z in self.e:
            print(f'Okay, {self.z.lower()}')
            self.q = True
            self.i()            
        elif self.z in self.h:
            for i in range(len(self.h)):
                print (self.m[i])
            self.i()                
        elif self.z in self.b:
            print (f"{self.z}? self.q is {self.q}")
            print (f"Changing self.q to {self.z}... {self.q} = {self.z}")            
            self.q = str(self.q).lower()
            self.q = self.q.capitalize()
        elif self.z == self.w[0]:
            print(f"{self.z.capitalize()}ed? Okay. Bye friend.")
            self.a.append(self.z)
            self.q = bool(self.q)            
        elif self.z == self.w[1]:
            print(f"Yes, you are: {self.z.capitalize()}!!!")            
        elif self.z == self.w[2]:
            print(f"You have {self.z}.")
            self.q = True
            self.x = 'win'
            self.y = 'game'            
        if self.q != True:         
            self.y = input("How many? ")
            if self.y in self.e:
                self.q = bool(self.q)
                self.i()
            elif self.y.isdigit() == True:
                print(f"{self.z.capitalize()}'s, eh?")
                self.y = int(self.y)                
            elif self.y.isdigit() != True:
                print(f"{self.y.capitalize()} is not a number.")
                print('')
                self.i()            
            self.x = input("Start at what number? ")
            if self.x in self.e:
                self.q = bool(self.q)
                self.i()                
            elif self.x.isdigit() == True:
                self.x = int(self.x)
                self.o()                
            elif self.x.isdigit() != True:
                print(f"{self.x.capitalize()} is not a number.")
                print('')
                self.i()
    def o(self):
        self.d = {}
        for self.x in range(int(self.x),int(self.y)+int(self.x)):      
            if str(self.z.isdigit()) == True and str(self.x.isdigit()) == False:
                exec("%d = %s" % (self.z,self.x))
            elif str(self.z.isdigit()) == False and str(self.x.isdigit()) == False:
                exec("%s = %s" % (self.z,self.x))                
            if str(self.x) != 1 and str(self.y) != 0:
                print(f"{self.z}{self.x}",)
                self.d.update({self.z:self.x})                
        s = f"Delivered {self.y} {self.z}'s to you."
        self.a.append(f'{s} ')
        print('')
        if self.q == "True":
            self.q == True
            pass
        elif self.q == False:
            self.i()
goto = Burger_Joint()
