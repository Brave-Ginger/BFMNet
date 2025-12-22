# BFMNet: Frequency-Aware Feature Fusion Driven Multi-Modal Cell Microscopic Image Segmentation Framework

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/PyTorch-2.0.1-orange.svg)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/)

## 📖 Introduction

**BFMNet** is a novel deep learning framework designed for the accurate and efficient segmentation of multi-modal cell microscopic images. As a core component of High-Content Imaging and Analysis (HCIA), this framework addresses common challenges in multi-modal segmentation such as missed cell detection in low-contrast regions, image degradation (noise/artifacts), and insufficient feature utilization.

BFMNet achieves state-of-the-art performance by integrating three core modules:
1.  **Weighted Bi-directional Feature Pyramid Network (BiFPN)**
2.  **Frequency-Aware Feature Fusion (FreqFusion)**
3.  **Mixed Local Channel Attention (MLCA)**

The model demonstrates robust generalization across Brightfield, Fluorescence, Phase Contrast (PC), and Differential Interference Contrast (DIC) modalities.

## 🚀 Key Features

* **High Precision:** Achieves **95.07% mAP50** and **96.72%** cell detection rate on dual-modal mouse glioma datasets.
* **High Efficiency:** operates at **41.93G FLOPs** with only **8.61M parameters** (tested on RTX 4070 Ti SUPER), making it significantly faster than Mask R-CNN and comparable to lightweight YOLO models.
* **Robustness:** Effectively handles blurred boundaries, artifacts, and noise without requiring manual parameter tuning or algorithm switching between modalities.

## 🛠️ Architecture

BFMNet consists of a backbone network coupled with three innovative modules:

1.  **BiFPN:** Replaces standard FPN to construct a weighted bidirectional cross-scale connection mechanism. It reduces missed detections in low-contrast regions by efficiently fusing shallow high-resolution details with deep semantic features.
2.  **FreqFusion:** A frequency-aware module that uses Adaptive Low-Pass/High-Pass Filters and an offset generator. It suppresses noise and sharpens cell boundaries, effectively handling image degradation.
3.  **MLCA:** A lightweight attention mechanism integrated into the bottleneck. It guides the model to focus on critical channels and hard-to-segment regions using a dual-branch structure (Local Average Pooling & Global Average Pooling).

> *Note: Please refer to the manuscript figures (Fig 3, 4, 5, 7) for detailed architectural diagrams.*

## ⚙️ Environment Setup

The code was developed and tested in the following environment:

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

# Install dependencies
pip install -r requirements.txt
