import rerun as rr

def main():
    rr.init("09_markdown", spawn=True)

    # Puedes loguear documentos Markdown para explicar tu visualización
    md_content = """
    # Mi Visualización
    
    Esta es una demostración de **Rerun**.
    
    ## Características
    - Puntos 3D
    - Imágenes
    - Gráficos
    
    Puedes usar listas, enlaces y formato básico.
    """
    
    rr.log("documentacion", rr.TextDocument(md_content))

if __name__ == "__main__":
    main()
