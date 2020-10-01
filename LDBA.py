class LDBA:
    def __init__(self):
        self.states={'q0','q1','q2','q3','trap'}
        self.final_states={'q1'}
        self.A=self.final_states
        self.current_state='q0'
        self.rp=2000
        self.rn=-100
        self.sinks={'trap'}
    def reward(self):
        if self.current_state in self.A:
            return self.rp
        if self.current_state in self.sinks:
            return self.rn
        return -1
    def acc(self):
        if self.current_state not in self.A:
            return
        self.A.remove(self.current_state)
        if(len(self.A)==0):
            self.A=self.final_states
    def step(self,c,e):
        '''
        update current state based on the input c and e
        '''
        if(self.current_state=='q0'):
            if(c and e):
                self.current_state='q1'
            elif(c and not e):
                self.current_state='q2'
            elif(not c and e):
                self.current_state='q3'
            else:
                self.current_state='q0'

        elif(self.current_state=='q2'):
            if(c and not e):
                self.current_state='q2'
            elif(e):
                self.current_state='q1'
            else:
                self.current_state='trap'
        
        elif(self.current_state=='q3'):
            if(c):
                self.current_state=='q1'
            else:
                self.current_state=='q3'

    def reset(self):
        self.A=self.final_states
        self.current_state='q0'