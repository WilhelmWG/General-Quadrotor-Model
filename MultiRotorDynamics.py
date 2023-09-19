import control as ct
import numpy as np
import scipy as sp
import utils as ut
from typing import List, Tuple
from scipy.spatial.transform import Rotation as R
from scipy.integrate import solve_ivp


g = 9.81


class Limb:
    def __init__(self, m, rot_vec, t_vec):
        self.m = m
        self.rot_vec = rot_vec 
        self.t_vec = t_vec

class Rotor(Limb):
    def __init__(self, m, rot_vec, t_vec, rps, C_q, C_t):
        super().__init__(m,rot_vec,t_vec)
        self.rps = rps #Rotations per second
        self.C_q = C_q
        self.C_t = C_t
    
    #returns the force in body frame
    def get_force_bf(self):
        force_rf = self.C_t*self.rps**2*np.array([0,0,1])
        force_rf = np.reshape(force_rf,(3,1))
        rot_mat = R.from_euler("zxy",self.rot_vec)
        rot_mat = rot_mat.as_matrix()
        force_bf = rot_mat@force_rf
        return force_bf
    
    def get_rps(self):
        return self.rps
    
    def set_rps(self, rps):
        self.rps = rps

class IMU(Limb):
    def __init__(self,m,rot_vec,t_vec):
        super().__init__(m,rot_vec,t_vec)

class DepthCamera(Limb):
    def __init__(self,m,rot_vec,t_vec,AoV,K,res):
        super().__init__(m,rot_vec,t_vec)
        self.AoV = AoV # Radians [Horizontal, Vertical, Diagonal]
        self.K = K #intrinsic matrix
        self.res = res
    
    def project_point(self, point_cf):
        u_hom = self.K@point_cf
        u = np.array([u_hom[0]/u_hom[2],u_hom[1]/u_hom[2]])
        u = np.round(u)

    def depth_frame(self, points_cf):
        depth_frame = np.zeros((self.res[1],self.res[0]))
        for point_cf in points_cf:
            u = self.project_point(point_cf)
            depth = np.linalg.norm(point_cf) #Don't know if depth = euclid distance or simply Z
            if (u[0] < self.res[0] and u[0] > 0) and (u[1] < self.res[1] and u[1] > 0):
                depth_frame[int(u[1]),int(u[0])] = depth
            
        return depth_frame

    


class MultiRotor:
    def __init__(self, m, rot_vec, t_vec, ang_vel, rotors: List[Rotor], dep_cams: List[DepthCamera], IMU: IMU):
        self.time = 0
        self.m = m
        
        self.rot_vec = rot_vec #Euler angles
        self.rot_vec_dot = np.zeros((3,))
        self.t_vec = t_vec #translation vector
        self.t_vec_dot = np.zeros((3,))
        self.ang_vel = ang_vel #Angular velocity
        self.ang_vel_dot = np.zeros((3,))
        self.R = R.from_euler("zxy",rot_vec).as_matrix() #Rotation Matrix
        self.R_dot = np.zeros((3,3))
        self.T = ut.transformation_matrix(self.R,t_vec)

        self.rotors = rotors
        self.dep_cams = dep_cams
        self.IMU = IMU
        self.J = self.calculate_inertial_tensor()

        self.t_vec_history = np.reshape(t_vec,(3,1))
        self.rot_vec_history = np.reshape(rot_vec,(3,1))
        
    
    def calculate_inertial_tensor(self):
        J = np.zeros((3,3),dtype=float)
        for rotor in self.rotors:
            t_vec = np.reshape(rotor.t_vec,(3,1))
            J += rotor.m*(sp.linalg.norm(t_vec)**2*np.eye(3)-(t_vec)@(t_vec.T))
            
        for dep_cam in self.dep_cams:
            t_vec = np.reshape(dep_cam.t_vec,(3,1))
            J += dep_cam.m*(sp.linalg.norm(t_vec)**2*np.eye(3)-(t_vec)@(t_vec.T))
        
        t_vec = np.reshape(self.IMU.t_vec,(3,1))
        J += self.IMU.m*(sp.linalg.norm(t_vec)**2*np.eye(3)-(t_vec)@(t_vec.T))
        
        return J
    
    def calculate_sum_of_forces_bf(self):
        sum_force = np.zeros((3,))
        for rotor in self.rotors:
            sum_force += np.reshape(rotor.get_force_bf(),(3,))
        rot_mat = R.from_euler("zxy",self.rot_vec)
        rot_mat = rot_mat.as_matrix()
        sum_force -= np.reshape(rot_mat@rotor.get_force_bf(),(3,))
        return sum_force

    def calculate_torque_from_thrust_bf(self):
        sum_torque = np.zeros((3,))
        for rotor in self.rotors:
            sum_torque += np.cross(rotor.t_vec,np.reshape(rotor.get_force_bf(),(3,))) # Cross Displacement with Force
        return sum_torque
    
    def calculate_reaction_torque_bf(self):
        sum_torque = np.zeros((3,))
        for rotor in self.rotors:
            sum_torque += np.reshape(rotor.get_force_bf()*rotor.C_q/rotor.C_t,(3,))*np.sign(rotor.get_rps())
        return sum_torque
    
    def calculate_sum_of_torques_bf(self):
        return self.calculate_reaction_torque_bf()+self.calculate_torque_from_thrust_bf()

    def get_depth_frames(self, obst_wf):
        T = ut.transformation_matrix(self.R,self.t_vec)
        obst_bf = ut.coordinate_transformation(T)
        print(obst_bf)


    def simulate_timestep(self,delta_t):
        rot_mat = R.from_euler("zxy",self.rot_vec)
        rot_mat = rot_mat.as_matrix()
        
        #Pose
        self.t_vec += self.t_vec_dot*delta_t #1a)
        self.R += self.R_dot*delta_t
        self.rot_vec = R.from_matrix(self.R).as_euler("zxy")
        
        #Angular velocity
        self.ang_vel += self.ang_vel_dot*delta_t
        
        #velocity
        self.ang_vel_dot = np.linalg.solve(self.J,(-np.cross(self.ang_vel,self.J@self.ang_vel)+self.calculate_sum_of_torques_bf())) #1d)
        self.t_vec_dot += rot_mat@self.calculate_sum_of_forces_bf()*delta_t #1b)
        self.R_dot = rot_mat@ut.skew(self.ang_vel) #1c)
        
        self.time += delta_t

        #update values
        self.T = ut.transformation_matrix(self.R,self.t_vec)
        self.t_vec_history = np.append(self.t_vec_history,np.reshape(self.t_vec,(3,1)),1)
        self.rot_vec_history = np.append(self.rot_vec_history,np.reshape(self.rot_vec,(3,1)),1)

