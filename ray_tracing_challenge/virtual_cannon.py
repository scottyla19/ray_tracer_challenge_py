def tick(env, proj):
    pos = proj.position + proj.velocity
    vel = proj.velocity + env.gravity + env.wind
    return Projectile(pos, vel)

class Projectile:
    def __init__(self, pos_pt, vel_vec):
        self.position = pos_pt
        self.velocity = vel_vec

class Environment:
    def __init__(self, grav_vec, wind_vec):
        self.gravity = grav_vec
        self.wind = wind_vec