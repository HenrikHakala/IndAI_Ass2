# Assignment 2

This is a Python project created for Assignment 2.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Project Structure

- `Transformers/` - Contains Jupyter notebooks and a model file for transformer-based experiments and similarity analysis.
  - `Transformer_ass2.ipynb`, `Transformers_Test.ipynb`, `Transformers_Similarity.ipynb`: Notebooks for various transformer tasks.
  - `circuitboard_classifier.pkl`: Pretrained model file.
- `AnomalyCLIP/` - Codebase for anomaly detection using CLIP, including training, testing, utilities, and results.
  - Includes scripts (`train.py`, `test.py`, etc.), utility modules, and subfolders for results, assets, and checkpoints.
- `CLIP/` - Contains submodules for anomaly detection and similarity analysis using CLIP.
  - `Anomaly/`: Includes `CLIP_Anomaly.ipynb` and related data/results for anomaly detection.
  - `Similarity/`: Includes `CLIP.ipynb` for similarity experiments.
- `Dataset_Circuitboard/` - Dataset folders for healthy, faulty, and validation circuit board images.
- `Random images/` - Example images (e.g., `house.jpeg`, `cat.webp`) for testing or demonstration.
- `checkpoints/` - Stores model checkpoints and logs for circuitboard experiments.
  - `circuitboard/`: Contains checkpoint files (`epoch_5.pth`, etc.) and logs.
- `requirements.txt` - Python dependencies for the project.
- `venv/` - Python virtual environment directory.

## Features

- Transformer-based experiments and similarity analysis
- Anomaly detection using CLIP
- Jupyter notebooks for interactive exploration
- Pretrained model and checkpoints included
- Dataset for circuit board classification and anomaly detection 