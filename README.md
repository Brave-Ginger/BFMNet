# BFMNet: Frequency-Aware Feature Fusion Driven Multi-Modal Cell Microscopic Image Segmentation Framework

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/PyTorch-2.0.1-orange.svg)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/)

## 📖 Introduction

**BFMNet** is a novel deep learning framework designed for the accurate and efficient segmentation of multi-modal cell microscopic images. [cite_start]As a core component of High-Content Imaging and Analysis (HCIA), this framework addresses common challenges in multi-modal segmentation such as missed cell detection in low-contrast regions, image degradation (noise/artifacts), and insufficient feature utilization[cite: 13, 14].

<div align="center">
  <img src="BFMNet/BFMNet Architecture.png" alt="BFMNet Architecture" width="100%">
</div>
[cite_start]BFMNet achieves state-of-the-art performance by integrating three core modules[cite: 15, 16, 17]:
1.  **Weighted Bi-directional Feature Pyramid Network (BiFPN)**
2.  **Frequency-Aware Feature Fusion (FreqFusion)**
3.  **Mixed Local Channel Attention (MLCA)**

[cite_start]The model demonstrates robust generalization across Brightfield, Fluorescence, Phase Contrast (PC), and Differential Interference Contrast (DIC) modalities[cite: 19].

## 🚀 Key Features

* [cite_start]**High Precision:** Achieves **95.07% mAP50** and **96.72%** cell detection rate on dual-modal mouse glioma datasets[cite: 18].
* [cite_start]**High Efficiency:** Operates at **41.93G FLOPs** with only **8.61M parameters** (tested on RTX 4070 Ti SUPER), making it significantly faster than Mask R-CNN and comparable to lightweight YOLO models[cite: 364, 365, 366].
* [cite_start]**Robustness:** Effectively handles blurred boundaries, artifacts, and noise without requiring manual parameter tuning or algorithm switching between modalities[cite: 14].

## 🛠️ Architecture

[cite_start]BFMNet consists of a backbone network coupled with three innovative modules[cite: 139]:

1.  **BiFPN:** Replaces standard FPN to construct a weighted bidirectional cross-scale connection mechanism. [cite_start]It reduces missed detections in low-contrast regions by efficiently fusing shallow high-resolution details with deep semantic features[cite: 15, 90].
2.  **FreqFusion:** A frequency-aware module that uses Adaptive Low-Pass/High-Pass Filters and an offset generator. [cite_start]It suppresses noise and sharpens cell boundaries, effectively handling image degradation[cite: 16, 93].
3.  **MLCA:** A lightweight attention mechanism integrated into the bottleneck. [cite_start]It guides the model to focus on critical channels and hard-to-segment regions using a dual-branch structure (Local Average Pooling & Global Average Pooling)[cite: 17, 96].

> *Note: Please refer to the manuscript figures (Fig 3, 4, 5, 7) for detailed architectural diagrams.*

## ⚙️ Environment Setup

[cite_start]The code was developed and tested in the following environment[cite: 209, 210, 363]:

* **OS:** Windows 10 64-bit
* **GPU:** NVIDIA GeForce RTX 4070 Ti SUPER (16GB)
* **Python:** 3.9
* **PyTorch:** 2.0.1
* **CUDA:** 11.8

### Installation

```bash
# Clone the repository
git clone [https://github.com/yourusername/BFMNet.git](https://github.com/yourusername/BFMNet.git)
cd BFMNet

# Create a virtual environment (optional but recommended)
conda create -n bfmnet python=3.9
conda activate bfmnet

# Install dependencies (ensure you have a requirements.txt)
pip install -r requirements.txt
