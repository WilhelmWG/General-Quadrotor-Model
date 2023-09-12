import control as ct
import numpy as np
import scipy as sp
from scipy.spatial.transform import Rotation as R
class QuadRotor:
    def __init__(self, m, rot_vec, t_vec, rotors):
        self.m = m
        self.rot_vec = rot_vec #
        self.t_vec = t_vec
        self.rotors = rotors

class Limb:
    def __init__(self, m, rot_vec, t_vec):
        self.m = m
        self.rot_vec = rot_vec 
        self.t_vec = t_vec

class Rotor(Limb):
    def __init__(self,m,rot_vec,t_vec, rps, C_q, C_t):
        super().__init__(m,rot_vec,t_vec)
        self.rps = rps #Rotations per second
        self.C_q = C_q
        self.C_t = C_t
    #returns the force in body frame
    def force_bf(self):
        return R.from_euler("zxy",self.rot_vec,)@self.C_t*self.rps**2*np.array([0,0,1])
    
    

class IMU(Limb):
    def __init__(self,m,rot_vec,t_vec):
        super().__init__(m,rot_vec,t_vec)
        
