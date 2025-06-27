import mesa

class ControlRodAgent(mesa.Agent):
    def __init__(
            self, model
        ):
        super().__init__(model)
        self.position = 0.5
        # 0 = rod fully out, 1 = rod fully inserted
    def step(self):
        #regulates the position in function of the power
        if self.model.power > 1.05:
            self.position += 0.01
            
        elif self.model.power < 0.95:
            self.position -= 0.01
        self.position = min(1.0,max(0.0,self.position))