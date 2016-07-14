import math

def phi(z):
    return 0.5 * (1.0 + math.erf(z/math.sqrt(2)))

# Calculate the probability for a range 
# m = mean, s = stand dev, low = lower bound, up = upper bound
# for low = - infinity use low = None
# for up  = + infinity use up = None
def prob_phi(m, s, low, up):
    s = float(s)

    ur = phi((up - m)/s)  if not up == None else 1.0
    lr = phi((low - m)/s) if not low == None else 0.0

    return round(ur - lr, 4)

# Tests
print prob_phi(0,1,-1.96, 1.96) == 0.95
print round(prob_phi(0,1,-1, 1), 2) == 0.68
print round(prob_phi(0,1,-1, 0), 2) == 0.34
print prob_phi(0,1,None, 0) == 0.5
print prob_phi(0,1,0, None) == 0.5
print prob_phi(0,1,None, None) == 1.0

# Examples
print prob_phi(190, 36, 154, 226) #Returns the range between 154 and 226 = 0.683
print prob_phi(190, 36, None, 118) #Returns the range between - infinity and 118 = 0.023
print prob_phi(190, 36, 226, None) #Returns the range between 226 and + infininity = 0.159
print prob_phi(190, 36, None, None) #Returns the range between - infinity and + infinity = 1.0
