import rerun as rr

def main():
    rr.init("02_shapes", spawn=True)

    # Loguear una caja (Box3D)
    # half_sizes define la mitad del ancho/alto/profundidad
    rr.log("formas/caja", rr.Boxes3D(half_sizes=[1, 1, 1], centers=[0, 0, 0], colors=[255, 0, 0]))

    # Loguear flechas (Arrows3D) para visualizar vectores
    rr.log("formas/flecha_x", rr.Arrows3D(origins=[2, 0, 0], vectors=[1, 0, 0], colors=[0, 255, 0]))
    rr.log("formas/flecha_y", rr.Arrows3D(origins=[0, 2, 0], vectors=[0, 1, 0], colors=[0, 0, 255]))

if __name__ == "__main__":
    main()
