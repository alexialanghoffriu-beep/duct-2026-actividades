Analizador de datos

Analiza la frecuencia de palabras en un archivo .txt y genera un gráfico de barras con las diez palabras más frecuentes. El análisis incluye la tokenización del texto y filtra palabras sin carga semántica comunes.

Requisitos
- Python 3.10 o superior
- pip
- matplotlib
- pytest

Instalación
git clone https://github.com/alexialanghoffriu-beep/duct-2026-actividades.git
cd duct-2026*actividades/AI
python -m venv venv
source venv/bin/activate    # en Windows: venv\Scripts\activate
pip install -r requirements.txt

Uso
# Ejecutar el Analizador
    python analizador.py
# Ejecutar las pruebas
    pytest -v
# El gráfico generado se guarda como grafico_frecuencias.png

Alexia Langhoff Riu - Diplomatura en Competencias Técnicas para Profesionales de Idiomas - 2026