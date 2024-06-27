import math
from scipy.stats import norm

class Option:
    def __init__(self, stock_price, vol, strike_price, time, risk_free, dividend_yield, option_type):
        self.stock_price = stock_price
        self.vol = vol
        self.strike_price = strike_price
        self.time = time
        self.risk_free = risk_free
        self.dividend_yield = dividend_yield
        self.option_type = option_type
        # if self.option_type.lower() == "call": calculating for all always and using put call parity 
        self.d1 = (math.log(self.strike_price / self.strike_price) + (self.risk_free + self.vol * self.vol / 2) * self.time) / (self.vol * math.sqrt(self.time))
        self.d2 = self.d1 - self.vol * math.sqrt(self.time)
        # else:  # for put just use put call parity.
        #     self.d1 = 5
            


    def intrinsic(self):
        if self.option_type.lower() == "call":
            return max(self.stock_price - self.strike_price, 0)
        else:
            return max(self.strike_price - self.stock_price, 0)

    def black_scholes_value(self):
        call_value = self.stock_price * norm.cdf(self.d1) - self.strike_price * math.exp(-self.risk_free * self.time) * norm.cdf(self.d2)
        put_value = call_value + self.strike_price * math.exp(-self.risk_free * self.time) - self.stock_price
        if self.option_type.lower() == "call":
            return(call_value)
        else:
            return(put_value)
        
    def iv(self, market_price): # calculate implied volatility given the market price.
        pass


    ## put in methods for black scholes_greeks

    def delta(self):
        pass

    def gamma(self):
        pass

    def theta(self):
        pass

    def rho(self):
        pass

    def vega(self):
        pass

