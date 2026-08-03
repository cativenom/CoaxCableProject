import json
import cmath
import unittest

class Solver:
    def __init__(self, conductor: str, dielectric: str, solve_type: str, a: float, b: float, ReZl: float, ImZl: float, freq: float, sigd=None, epd=None, sigc=None, mur=None):
        with open("data/materials.json", "r") as file:
                data = json.load(file)
                
        # Material Stuff
        if conductor is not None:
            self.sigc = data["conductor"][conductor]["sigc"]
        else:
            self.sigc = sigc
            
        if dielectric is not None:
            self.sigd = data["dielectric"][dielectric]["sigd"]
            self.epd = data["dielectric"][dielectric]["epd"]
            self.mur = data["dielectric"][dielectric]["mur"]
            if self.sigd == "None":
                self.sigd = 0
        else:
            self.sigd = sigd
            self.epd = epd
            self.mur = mur
            
        # Provided Stuff
        self.solve_type = solve_type
        self.a = a
        self.b = b
        self.zl = complex(ReZl, ImZl)
        self.f = freq
        
        # Not Provided Stuff
        self.eps_0 = 8.85419e-12
        self.mu_0 = 4*cmath.pi*(10**-7)
        self.ref = complex
        self.vswr = complex   
        self.G = float 
        
        self.ep = self.eps_0 * self.epd
        self.mu = self.mur * self.mu_0

        
    def _dist_params(self):
        c = 2 * cmath.pi * self.ep
        c = c / cmath.log(self.b / self.a)
        
        g = self.sigd * c
        g = g / self.ep
        
        l = self.mu * cmath.log(self.b / self.a)
        l_den = 2 * cmath.pi
        l = l / l_den
        
        r = cmath.pi * self.f * self.mu_0
        r = r / self.sigc
        r = cmath.sqrt(r)
        r = r / l_den
        a_inv = self.a ** -1
        b_inv = self.b ** -1
        r_prod = a_inv + b_inv
        r = r * r_prod
        
        return g, c, l, r
        
    def _char_impedance(self):
        g_pr, c_pr, l_pr, r_pr = self._dist_params()
        self.rl = complex(r_pr, 2 * cmath.pi * self.f * l_pr)
        self.gc = complex(g_pr, 2 * cmath.pi * self.f * c_pr)
        
        self.gamma = cmath.sqrt(self.rl * self.gc)
        print(self.gamma)
        
        z0 = cmath.sqrt(self.rl / self.gc)
        return z0
    
    def _ref_coeff(self): 
        if abs(self.zl) == 0: 
          self.ref = -1
        else:
          self.ref = (self.zl-self.z0)/(self.zl+self.z0)
        return self.ref

    def _VSWR(self):
        if abs(self.zl) == 0:
          self.vswr = cmath.inf
        else:
          self.vswr = (1+abs(self.ref))/(1-abs(self.ref))
        return self.vswr
    
    def _gain(self):
        # self.G =  10 * cmath.log10(cmath.exp(-2*self.gamma.real*self.l))
        self.G = 10 * cmath.log10(1 - (abs(self.ref) ** 2))
        return self.G.real

    
    def solve(self):
        self.z0 = self._char_impedance()
        self.ref = self._ref_coeff()
        self.vswr = self._VSWR()
        self.G = self._gain()
        print(self.z0)
        # print(self.ref)
        # print(self.vswr)
        # print(self.G)
        
""" Abandoned attempt to solve an L matching network with discrete components """
        
    # def react_to_comp(self, X):
    #     if X > 0:
    #         return('L', X / self.w)
    #     else:
    #         return('C', -1 / (X * self.w))
        
    # def sus_to_comp(self, B):
    #     if B > 0:
    #         return('L', B / self.w)
    #     else:
    #         return('C', -1 / (B * self.w))
        
    # def idk what im doin
    # def l_match(self):
    #     # https://www.silabs.com/documents/public/application-notes/an1275-imp-match-for-network-arch.pdf
    #     # https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Fundamentals_of_Microwave_and_RF_Design_(Steer)/10%3A_Impedance_Matching/10.05%3A__Dealing_with_Complex_Loads
        
    #     w = 2 * cmath.pi * self.f
    


if __name__ == "__main__":
    # solv = Solver("Copper", "Air", "Shorted", 2, 4, 6, 1, 1*10**9)
    # solv.solve()

    # solv = Solver("Copper", "Air", "Shorted", 2, 4, 6, 1, 1*10**9)
    # solv.solve()

    rg58 = Solver("Copper", "Polyethylene", "open", 0.000405, 0.001475, 1, 1, 1000000000)
    rg58.solve()

    # rg59 = Solver("Copper", "Polyethylene", "Dunno", 0.00029, 0.00185, 1, 1, 1000000000)
    # rg59.solve()

    # rg8 = Solver("Copper", "Polyethylene", "Dunno", 0.001085, 0.00362, 1, 1, 1000000000)
    # rg8.solve()

    # rg142 = Solver("Copper", "Polyethylene", "Dunno", 0.00047, 0.00151, 1, 1, 1000000000)
    # rg142.solve()

    # airlossless = Solver("Copper", "Air", "Dunno", 0.0005, 0.0015, 1, 1, 1000000000)
    # airlossless.solve()
    

    
    
        
        
        