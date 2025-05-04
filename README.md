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

ASSIGNMENT2/
├── Augmenter/                       # Data augmentation notebooks
│   └── Augmentation.ipynb
├── CLIP/
│   ├── Anomaly/                     # Anomaly detection using CLIP
│   │   ├── checkpoints/            # Trained model checkpoints
│   │   ├── Data/                   # Anomaly detection data
│   │   ├── results/                # Output results
│   │   ├── CLIP_Anomaly.ipynb     # Main anomaly detection notebook
│   │   └── Edits.txt              # Notes or change log
│   └── Similarity/                 # Similarity analysis with CLIP
│       ├── CLIP.ipynb
│       ├── fine_tuned_clip.pt
│       └── fine_tuned_clip_last_layer.pt
├── Dataset_Circuitboard/           # Original dataset
├── Dataset_Circuitboard_augmented/# Augmented dataset
├── Dataset_Circuitboard_labeled/  # Labeled dataset for classification
├── Random images/                  # Sample images for testing
├── Transformers/                   # Transformer-based experiments
│   ├── circuitboard_classifier.pkl# Pretrained classifier model
│   ├── image_similarity.ipynb     # Image similarity with transformers
│   ├── Transfer_learning.ipynb    # Main notebook for transfer learning
│   └── Transfer_learning_Test.ipynb# Exploratory notebook
├── venv/                           # Python virtual environment
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation

## Features

- Transformer-based experiments and similarity analysis
- Anomaly detection using CLIP
- Jupyter notebooks for interactive exploration
- Pretrained model and checkpoints included
- Dataset for circuit board classification and anomaly detection 

All the ipynb should be runnable except the anomaly one. This needs the terminal commands to be runnable. One can simply follow the order of the CLIP\Anomaly\CLIP_Anomaly.ipynb