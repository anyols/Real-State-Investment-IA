import pandas as pd
import os
import matplotlib.pyplot as plt
from IPython.display import display, Image
import shutil

# Llegir el fitxer CSV
csv_path = "./_annotations.csv"
df = pd.read_csv(csv_path)

# Crear una nova columna per a les etiquetes
df["labels"] = 0


# Funció per mostrar la imatge i obtenir l'etiqueta
def get_label_for_image(image_path, classe):
    # Mostrar la imatge
    plt.imshow(plt.imread(image_path))
    plt.title(classe)
    plt.axis("off")
    plt.show()

    # Obtenir l'input de l'usuari
    while True:
        try:
            label = int(
                input(f"Introdueix l'etiqueta per a la classe {classe} (0 o 1): ")
            )
            if label in [0, 1]:
                return label
            else:
                print("Si us plau, introdueix 0 o 1.")
        except ValueError:
            print("Input no vàlid. Introdueix 0 o 1.")


# Recorre cada fila del dataframe per mostrar la imatge i obtenir l'etiqueta
for idx, row in df.iterrows():
    image_filename = row[0]
    image_path = os.path.join(
        "./images/", image_filename
    )  # Canvia '/path/to/images' per el camí correcte
    if os.path.exists(image_path):
        label = get_label_for_image(image_path, df.at[idx, "class"])
        df.at[idx, "labels"] = label
    else:
        print(f"No s'ha trobat la imatge: {image_path}")

# Desar el dataframe actualitzat en un nou fitxer CSV
output_csv_path = "./_annotations_regions.csv"
df.to_csv(output_csv_path, index=False)
print(f"Fitxer actualitzat desat a: {output_csv_path}")
