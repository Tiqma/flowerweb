import matplotlib.pyplot as plt
import io
import base64
from flowers.flowers import add_flower

# Funktion för att läsa in blomdata från en fil
def read_flowers_data(filename):
    flowers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 6:
                flower = {
                    'namn': parts[0].strip(),
                    'vetenskapligt_namn': parts[1].strip(),
                    'vattnings_intervall': int(parts[2].strip()),
                    'vatten_ml': int(parts[3].strip()),
                    'light': parts[4].strip(),
                    'watering': parts[5].strip()
                }
                flowers.append(flower)
    return flowers


def add_flowers_from_txt_to_database():
    flowers_data = read_flowers_data("flowers_data.txt")
    for flower in flowers_data:
        add_flower(flower['vetenskapligt_namn'][:2], flower['namn'], '', flower['watering'])
    
    return

add_flowers_from_txt_to_database()

# Funktion för att plotta vattningsintervaller
def plot_watering_intervals(flowers):
    """Skapar en graf över hur ofta varje blomma ska vattnas och returnerar den som base64-bild."""
    names = [f['namn'] for f in flowers]
    intervals = [f['vattnings_intervall'] for f in flowers]

    plt.figure(figsize=(10, 6))
    plt.bar(names, intervals, color='skyblue')
    plt.title("Vattningsintervall för olika blommor")
    plt.xlabel("Blommor")
    plt.ylabel("Vattningsintervall (dagar)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return img_base64