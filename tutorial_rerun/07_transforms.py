import rerun as rr
import numpy as np

def main():
    rr.init("07_transforms", spawn=True)

    # Definir una jerarquía con transformaciones
    # El 'sol' está en el centro
    rr.log("sistema_solar/sol", rr.Points3D([[0, 0, 0]], radii=2, colors=[255, 255, 0]))

    for t in range(100):
        rr.set_time_sequence("step", t)

        # La tierra orbita alrededor del sol
        angle = t * 0.1
        translation = [np.cos(angle)*5, np.sin(angle)*5, 0]
        
        # Transform3D aplica a todo lo que esté "debajo" en la jerarquía
        # Logueamos una transformación en "sistema_solar/tierra_frame"
        # Todo lo que logueemos bajo "sistema_solar/tierra_frame/..." se moverá con esto.
        rr.log("sistema_solar/tierra_frame", rr.Transform3D(translation=translation))
        
        # Ahora logueamos la tierra RELATIVA a 'tierra_frame' (en 0,0,0 de ese frame)
        rr.log("sistema_solar/tierra_frame/tierra", rr.Points3D([[0, 0, 0]], radii=0.5, colors=[0, 100, 255]))
        
        # Y la luna relativa a la tierra
        moon_angle = t * 0.5
        moon_pos = [np.cos(moon_angle)*1.5, np.sin(moon_angle)*1.5, 0]
        rr.log("sistema_solar/tierra_frame/tierra/luna", rr.Points3D([moon_pos], radii=0.2, colors=[150, 150, 150]))

if __name__ == "__main__":
    main()
