import rerun as rr

def main():
    rr.init("06_hierarchy", spawn=True)

    # Rerun usa rutas tipo sistema de archivos para organizar entidades
    # Aquí creamos una jerarquía: mundo -> robot -> brazo -> mano
    
    rr.log("mundo/suelo", rr.Boxes3D(half_sizes=[10, 10, 0.1], centers=[0, 0, -0.1], colors=[50, 50, 50]))
    
    rr.log("mundo/robot/cuerpo", rr.Boxes3D(half_sizes=[1, 1, 1], centers=[0, 0, 1]))
    rr.log("mundo/robot/brazo", rr.Boxes3D(half_sizes=[0.2, 0.2, 2], centers=[0, 0, 4], colors=[200, 100, 0]))
    
    # Nota cómo en el visor puedes activar/desactivar 'mundo', 'robot', etc.
    # La jerarquía ayuda a mantener organizado el visualizador.

if __name__ == "__main__":
    main()
