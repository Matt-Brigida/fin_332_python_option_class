import math

class Option:
    def __init__(self, stock_price, vol, strike_price, time, risk_free, dividend_yield, option_type):
        self.stock_price = stock_price
        self.vol = vol
        self.strike_price = strike_price
        self.time = time
        self.risk_free = risk_free
        self.dividend_yield = dividend_yield
        self.option_type = option_type
        if self.option_type == "Call":
            self.d1 = (math.log(self.strike_price / self.strike_price) + (self.risk_free + self.vol * self.vol / 2) * self.time) / (self.vol * math.sqrt(self.time))
            self.d2 = self.d1 - self.vol * math.sqrt(self.time)
        else:
            self.d1 = 5
            


    def intrinsic(self):
        if self.option_type == "Call":
            return max(self.stock_price - self.strike_price, 0)
        else:
            return max(self.strike_price - self.stock_price, 0)

#    def black_scholes_value(self):
        
