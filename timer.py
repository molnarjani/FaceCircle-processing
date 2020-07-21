class Timer(object):
    def __init__(self, tick_miliseconds, callback_function=None):
        self.saved_time = millis()
        self.tick = tick_miliseconds
        self.callback_function = callback_function
        self.started = False
    
    def start(self):
        self.started = True
        
    def stop(self):
        self.started = False
    
    def step(self):
        if self.started:
            passed_time = (millis() - self.saved_time)
            if (passed_time > self.tick):
                self.saved_time = millis()
                if self.callback_function is not None:
                    self.callback_function()
                
    
        
