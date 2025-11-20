import rerun as rr

def main():
    # 1. Inicializar Rerun
    # "manipulator_tutorial" es el ID de la aplicación
    # spawn=True abre el visor automáticamente
    rr.init("manipulator_tutorial_01", spawn=True)

    # 2. Visualizar el origen (World Frame)
    # Usamos flechas para indicar los ejes X, Y, Z
    rr.log("world/x_axis", rr.Arrows3D(vectors=[[1, 0, 0]], colors=[[255, 0, 0]], radii=0.05))
    rr.log("world/y_axis", rr.Arrows3D(vectors=[[0, 1, 0]], colors=[[0, 255, 0]], radii=0.05))
    rr.log("world/z_axis", rr.Arrows3D(vectors=[[0, 0, 1]], colors=[[0, 0, 255]], radii=0.05))

    print("Paso 1 completado: Se ha inicializado Rerun y dibujado el sistema de coordenadas.")

if __name__ == "__main__":
    main()
