from experta import *
import ast


class ApendicitsDiagnosis(KnowledgeEngine):
    username = "", 


    @DefFacts()
    def needed_data(self):
        """ 
        This is a method which is called everytime engine.reset() is called.
        It acts like a constructor to this class.
        """        
        yield Fact(DAppendicitis = 'true')
        print("Hi! Let me help you to diagnose Apendicitis \n\n Plese go check Doctor in order to get actual diagnosis and further treatment\n\nI will ask you 10 questions.\n\n")
        

    @Rule(Fact(DAppendicitis = 'true'),NOT(Fact(name=W())),salience = 540)
    def ask_name(self):
        self.username = input("What's your name?\n")
        self.declare(Fact(name=self.username))

    
    @Rule(Fact(DAppendicitis='true'), NOT (Fact(lowerabdomenpain = W())),salience = 520)
    def hasLowerabodmenpain(self):
        self.lowerabdomenpain = input("\nDo you feel pain in the lower right abdomen that appear suddenly?\nPlease type y/n\n")
        self.lowerabdomenpain = self.lowerabdomenpain.lower()
        self.declare(Fact(lowerabdomenpain = self.lowerabdomenpain.strip().lower()))
        if self.lowerabdomenpain == 'y':
            self.declare(Fact(value1 = 0.9 ))


    @Rule(Fact(DAppendicitis='true'), NOT (Fact(heartabdomenpain = W())),salience = 500)
    def hasHeartabodmenpain(self):
        self.heartabdomenpain = input("\nDo you feel abdominal pain that start from the heart then moves to lower abdomem?\nPlease type y/n\n")
        self.heartabdomenpain = self.heartabdomenpain.lower()
        self.declare(Fact(heartabdomenpain = self.heartabdomenpain.strip().lower()))
        if self.heartabdomenpain == 'y':
            self.declare(Fact(value2 = 0.8 ))

    @Rule(Fact(DAppendicitis='true'), NOT (Fact(coughabdomenpain = W())),salience = 480 )
    def hasCoughabdomenpain(self):
        self.coughabdomenpain = input("\nDo you fell lower right abdmoinal pain that get worse when walk, and choug?\nPlease type y/n\n")
        self.coughabdomenpain = self.coughabdomenpain.lower()
        self.declare(Fact(coughabdomenpain = self.coughabdomenpain.strip().lower()))
        if self.coughabdomenpain == 'y':
            self.declare(Fact(value3 = 0.9 ))

    @Rule(Fact(DAppendicitis='true'), NOT (Fact(Nuaseavomit = W())),salience = 460)
    def hasNauseavomit(self):
        self.Nuaseavomit = input("\nDo you experience nuasea and vomit?\nPlease type y/n\n")
        self.Nuaseavomit = self.Nuaseavomit.lower()
        self.declare(Fact(Nuaseavomit = self.Nuaseavomit.strip().lower()))
        
        if self.Nuaseavomit == 'y':
            self.declare(Fact(value4 = 0.6 ))


    @Rule(Fact(DAppendicitis='true'), NOT (Fact(lossappetite = W())),salience = 440)
    def hasLossappetite(self):
        self.lossappetite = input("\nDo you fell loss of appetite\nPlease type y/n\n")
        self.lossappetite = self.lossappetite.lower()
        self.declare(Fact(lossappetite = self.lossappetite.strip().lower()))

        if self.lossappetite == 'y':
            self.declare(Fact(value5 = 0.8 ))


    @Rule(Fact(DAppendicitis='true'), NOT (Fact(mildfever = W())),salience = 420)
    def hasMildfever(self):
        self.mildfever = input("\nDo experience mild fever\nPlease type y/n\n")
        self.mildfever = self.mildfever.lower()
        self.declare(Fact(mildfever = self.mildfever.strip().lower()))
        if self.mildfever == 'y':
            self.declare(Fact(value6 = 0.9 ))
    
    @Rule(Fact(DAppendicitis='true'), NOT (Fact(diarrhea = W())),salience = 400)
    def hasDiarrhea(self):
        self.diarrhea = input("\nDo you experiece diarrhea?\nPlease type y/n\n")
        self.diarrhea = self.diarrhea.lower()
        self.declare(Fact(diarrhea = self.diarrhea.strip().lower()))
        if self.diarrhea == 'y':
            self.declare(Fact(value7 = 0.8 ))

    @Rule(Fact(DAppendicitis='true'), NOT (Fact(stomachbloat = W())),salience = 380)
    def hasSctomachBloat(self):
        self.stomachbloat = input("\nDo you experience stomachbloat?\nPlease type y/n\n")
        self.stomachbloat=self.stomachbloat.lower()
        self.declare(Fact(stomachbloat = self.stomachbloat.strip().lower()))
        if self.stomachbloat == 'y':
            self.declare(Fact(value8 = 0.9 ))

    @Rule(Fact(DAppendicitis='true'), NOT (Fact(constipation = W())),salience = 360)
    def hasConstipation(self):
        self.constipation = input("\nDo you experience constipation?\nPlease type y/n\n")
        self.constipation = self.constipation.lower()
        self.declare(Fact(constipation = self.constipation.strip().lower()))
        if self.constipation == 'y':
            self.declare(Fact(value9 = 0.9 ))


    @Rule(Fact(DAppendicitis='true'), NOT (Fact(fart = W())),salience = 320)
    def hasFart(self):
        self.fart = input("\nDo you can't fart?\nPlease type y/n\n")
        self.fart = self.fart.lower()
        self.declare(Fact(fart = self.fart.strip().lower()))
        if self.fart == 'y':
            self.declare(Fact(value10 = 0.7 ))


    @Rule(Fact(DAppendicitis='true'),Fact(lowerabdomenpain = 'y'), Fact(heartabdomenpain = 'y'), Fact(coughabdomenpain = 'y'),Fact(Nuaseavomit = 'y'),
    Fact(lossappetite = 'y'),Fact(mildfever = 'y'),Fact(diarrhea = 'y'),Fact(stomachbloat= 'y'),Fact(constipation='y'),
    Fact(fart = 'y'))
    def disease_0(self):
        print("\nYou are diagnosed with Apendicits")
    
    @Rule(Fact(DAppendicitis='true'),Fact(lowerabdomenpain = 'y'), Fact(heartabdomenpain = 'n'), Fact(coughabdomenpain = 'y'),Fact(Nuaseavomit = 'y'),
    Fact(lossappetite = 'y'),Fact(mildfever = 'n'),Fact(diarrhea = 'y'),Fact(stomachbloat= 'y'),Fact(constipation='n'),
    Fact(fart = 'y'))
    def disease_1(self):
        print("\nYou are diagnosed with Intestine Inflammation")
    
    @Rule(Fact(DAppendicitis='true'),Fact(lowerabdomenpain = 'n'), Fact(heartabdomenpain = 'y'), Fact(coughabdomenpain = 'n'),Fact(Nuaseavomit = 'n'),
    Fact(lossappetite = 'y'),Fact(mildfever = 'n'),Fact(diarrhea = 'n'),Fact(stomachbloat= 'y'),Fact(constipation='n'),
    Fact(fart = 'n'))
    def disease_2(self):
        print("\nYou may have an ulcer")

    @Rule(Fact(DAppendicitis='true'), AND(Fact(value1=0.9), Fact(value3=0.9), Fact(value6=0.9), Fact(value8=0.9), Fact(value9=0.9)), NOT(OR(Fact(value2=0.7),Fact(value4=0.6),Fact(value5=0.8),Fact(value7=0.7),Fact(value10=0.7))))
    def disease_3(self):
        print('\n You are highly chance diagnosed with Apendicits. \n Please go to the Doctor immediatly(less than 24 hour) to get CT Scan')
    
    @Rule(Fact(DAppendicitis='true'), NOT(OR(Fact(value1=0.9), Fact(value3=0.9), Fact(value6=0.9), Fact(value8=0.9), Fact(value9=0.9)), EXISTS(Fact(value2=0.7),Fact(value4=0.6),Fact(value5=0.8),Fact(value7=0.7),Fact(value10=0.7))))
    def disease_4(self):
        print('\n We are not sure what happen to you')
    
    
    
    @Rule(Fact(DAppendicitis='true'), NOT(AND(Fact(value1=0.9), Fact(value3=0.9), Fact(value6=0.9), Fact(value8=0.9), Fact(value9=0.9))))
    def disease_6(self):
        print('\n We are not sure what happen to you')
    
    

    
       
  


if __name__ == "__main__":
    engine = ApendicitsDiagnosis()
    engine.reset()
    engine.run()
    
   