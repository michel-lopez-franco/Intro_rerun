import rerun as rr
import numpy as np

def main():
    rr.init("01_points_3d", spawn=True)

    # Generar 10 puntos aleatorios
    positions = np.random.uniform(-5, 5, size=(10, 3))
    colors = np.random.uniform(0, 255, size=(10, 3)).astype(np.uint8)

    # Loguear puntos estáticos
    # Points3D es el arquetipo para nubes de puntos
    rr.log("puntos_aleatorios", rr.Points3D(positions, colors=colors, radii=0.5))

if __name__ == "__main__":
    main()
