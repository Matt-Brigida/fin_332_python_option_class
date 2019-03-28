

class Option:
    def __init__(self, stock_price, vol, strike, time, risk_free, dividend_yield):
        self.stock_price = stock_price
        self.vol = vol
        self.strike = strike
        self.time = time
        self.risk_free = risk_free
        self.dividend_yield = dividend_yield

    def intrinsic(self):
        return max(self.stock_price - self.strike, 0)

    def black_scholes_value(self)
