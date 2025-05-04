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
  - `Transfer_learning,ipynb` This is for circuitboard dataset
  - `Transfer_learnign_Test.ipynb` This i only to familiaries with transfer learning
  - `image_similarity.ipynb` This i only to familiaries with transfer learning

- `AnomalyCLIP/` - Codebase for anomaly detection using CLIP, including training, testing, utilities, and results.
  - Includes scripts (`train.py`, `test.py`, etc.), utility modules, and subfolders for results, assets, and checkpoints.

- `CLIP/` - Contains submodules for anomaly detection and similarity analysis using CLIP.
  - `Anomaly/`: Includes `CLIP_Anomaly.ipynb` and related data/results for anomaly detection.
  - `Similarity/`: Includes `CLIP.ipynb` for similarity experiments.
- `Dataset_Circuitboard/` - This is the origianl dataset
- `Dataset_Circuitboard_augmented/` - This is the augmented dataset
- `Dataset_Circuitboard_labeld/` - This dataset contains labels
- `Random images/` - Example images (e.g., `house.jpeg`, `cat.webp`) for testing or demonstration.
- `requirements.txt` - Python dependencies for the project.

## Features
- Transformer-based experiments and similarity analysis
- Anomaly detection using CLIP
- Jupyter notebooks for interactive exploration
- Pretrained model and checkpoints included
- Dataset for circuit board classification and anomaly detection 

## Usage
- All python notebooks should be runnable, except `CLIP_Anomaly.ipynb` this one need the therminal commands to be run first. The commands are listed inside the notebook