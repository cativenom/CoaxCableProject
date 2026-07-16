import json
import cmath

class Solver:
    def __init__(self, conductor: str, dielectric: str, solve_type: str, a: float, b: float, c: float, length: float, ReZl: float, ImZl: float, freq: float, sigd=None, epd=None, sigc=None, mur=None):
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
        else:
            self.sigd = sigd
            self.epd = epd
            self.mur = mur
            
        # Provided Stuff
        self.solve_type = solve_type
        self.a = a
        self.b = b
        self.c = c
        self.l = length
        self.zl = complex(ReZl, ImZl)
        self.f = freq
        
        # Not Provided Stuff
        self.eps_0 = 0.000000000007754
        self.mu_0 = 4*cmath.pi*(10**-7)
        
    def _dist_params(self):
        c = 2 * cmath.pi * self.epd
        c = c / cmath.log(self.b / self.a)
        
        g = self.sigd * c
        g = g / self.epd
        
        l = self.mur * self.mu_0 * cmath.log(self.b / self.a)
        l_den = 2 * cmath.pi
        l = l / l_den
        
        r = cmath.pi * self.f * self.mur * self.mu_0
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
        
        z0 = cmath.sqrt(self.rl / self.gc)
        return z0
    
    def solve(self):
        self.z0 = self._char_impedance()
        print(self.z0)
        
solv = Solver("Copper", "Air", "Shorted", 2, 4, 6, 1, 1, 1, 1*10**9)
solv.solve()