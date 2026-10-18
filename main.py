import numpy as np
# from scipy.spatial.transform import Rotation as R


def r_x(theta, psi, r):
    return r * np.cos(theta) * np.cos(psi)

def r_y(theta, psi, r):
    return r * np.sin(theta) * np.cos(psi)

def r_z(psi, r):
    return r * np.sin(psi)

'''
def local_global(base_plane, local_vectors):
    def u_x(base_plane):
        return np.array([(base_plane[0]) / global p), (base_plane[1] / global p), (base_plane[2] / global p)])
    def u_y()
    return 
'''
def u_x(base_vector):
    length = np.linalg.norm(base_vector)
    return base_vector / length
def u_y(theta):
    return np.array([-np.sin(theta), np.cos(theta), 0.0])
def u_z(theta, psi, base_plane):
    cross_product = np.cross(u_x(base_plane), u_y(theta))
    transformation = np.array([-np.cos(theta) * np.sin(psi), -np.sin(theta) * np.sin(psi), np.cos(psi)])
    if np.allclose(cross_product, transformation):
        return cross_product
    else:
        return ValueError("Error: The cross product does not match the expected transformation vector.")

def local_global(base_vector, theta, psi, local_vectors):
    ux = u_x(base_vector)
    uy = u_y(theta)
    uz = u_z(theta, psi, base_vector)
    return local_vectors[0] * ux + local_vectors[1] * uy + local_vectors[2] * uz

##############################


# "p" denotes the upper arm. theta_1 is the angle to x-axis, theta_2 is the angle to xy-plane. The angles are in degrees converted to radians. 
p = 300
phi_x = 30
phi_z = 45
theta_1 = np.radians(phi_x)
theta_2 = np.radians(phi_z)


r_p = np.array([r_x(theta_1, theta_2, p), r_y(theta_1, theta_2, p), r_z(theta_2, p)])
r_p_x, r_p_y, r_p_z = r_p


# "q" denotes the forearm. Imagin looking down in the barrel of the arm, as the new local axis'. theta_3 is the angle from x' axis toward y' axis, theta_4 is the angle toward z'axis.
q = 200
psi_x = 30
psi_z = 45
theta_3 = np.radians(psi_x)
theta_4 = np.radians(psi_z)


q_local = np.array([r_x(theta_3, theta_4, q), r_y(theta_3, theta_4, q), r_z(theta_4, q)])
r_q_x, r_q_y, r_q_z = q_local


#np.array([u_x(r_p), u_y(theta_1), u_z(theta_1, theta_2, r_p)])
r_q = np.array([r_q_x * u_x(r_p) + r_q_y * u_y(theta_1) + r_q_z * u_z(theta_1, theta_2, r_p)])

r_wrist = r_p + r_q

print("Elbow position (r_p):   ", np.round(r_p, 2))
print("Forearm vector (r_q):   ", np.round(r_q, 2))
print("Length of r_q check:    ", np.round(np.linalg.norm(r_q), 2))
print("Wrist position (r_wrist):", np.round(r_wrist, 2))
