import rerun as rr
import numpy as np
import time

def main():
    rr.init("10_complete_sim", spawn=True)
    
    # Configuración
    num_particles = 50
    positions = np.random.normal(0, 2, size=(num_particles, 3))
    velocities = np.random.normal(0, 0.1, size=(num_particles, 3))
    colors = np.random.uniform(0, 255, size=(num_particles, 3)).astype(np.uint8)
    
    # Documentación
    rr.log("info", rr.TextDocument("# Simulación de Partículas\nPartículas rebotando en una caja."))
    
    # Caja delimitadora
    box_size = 5.0
    # fill_mode="wireframe" solo dibuja las líneas (requiere versión reciente de Rerun, si falla usar Lines3D)
    # Nota: Boxes3D no tiene fill_mode en todas las versiones, si da error se verá sólido.
    # Para asegurar wireframe visual, a veces se usan LineStrips3D, pero Boxes3D es lo estándar.
    rr.log("mundo/caja", rr.Boxes3D(half_sizes=[box_size, box_size, box_size], centers=[0,0,0], colors=[255, 255, 255]))

    for t in range(200):
        rr.set_time_sequence("frame", t)
        
        # Actualizar física
        positions += velocities
        
        # Rebote simple
        for i in range(3):
            mask_lower = positions[:, i] < -box_size
            mask_upper = positions[:, i] > box_size
            velocities[mask_lower, i] *= -1
            velocities[mask_upper, i] *= -1
            positions[mask_lower, i] = -box_size
            positions[mask_upper, i] = box_size
            
        # Loguear partículas
        rr.log("mundo/particulas", rr.Points3D(positions, colors=colors, radii=0.2))
        
        # Loguear energía cinética promedio
        kinetic_energy = 0.5 * np.sum(velocities**2) / num_particles
        rr.log("metricas/energia_cinetica", rr.Scalars(kinetic_energy))
        
        # Loguear velocidad de una partícula destacada (la 0)
        rr.log("metricas/vel_p0", rr.Scalars(np.linalg.norm(velocities[0])))
        rr.log("mundo/particula_destacada", rr.Points3D([positions[0]], colors=[255, 0, 0], radii=0.4))
        
        time.sleep(0.02)

if __name__ == "__main__":
    main()
