class Options:
    def __init__(self, opt):
        self.opt = opt

    def display(self):
        if self.opt == 0:
            return """
            _______
        ---'   ____)
               (_____)
               (_____)
               (____)
         ---.__(___)
            """
        elif self.opt == 1:
            return """         
                _______
            ---'    ____)____
                        ______)
                       _______)
                     _______)
            ---.__________)
            """
        elif self.opt == 2:
            return """
                _______
            ---'   ____)____
                      ______)
                    __________)
                  (____)
             ---.__(___)
            """
