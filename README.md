## 🧠 Reduced-Order Modeling for Hypersonic Scramjet Performance

This repository contains all code related to the development, testing, and deployment of a Reduced-Order Model (ROM) for predicting the performance of hypersonic scramjet engines. This is a draft and the code is very scattered. The model uses a Tensorflow architype which will be improved upon with more complex models for the final project. The system integrates CFD-based modeling, machine learning, and efficient sampling techniques to enable fast and accurate inference.

---

### 📂 Project Structure

#### 🧠 `ReducedOrderModel-Numerical/`
Contains the core implementation of the Reduced-Order Model. The trained model is saved as a `.pkl` file and serves as the foundation for all downstream applications.

#### 🌐 `predict.py`
Loads the serialized ROM from the `ReducedOrderModel-Numerical` module and provides a simple interface for inference. This script powers the **web application** used for real-time predictions.

#### 📊 `ReducedOrderModel-Contour/`
Uses the same core ROM to generate **visual outputs** (e.g., contour maps). Includes testing scripts and examples for interacting with and visualizing model inputs and outputs.

#### 🧪 `neuralnetworks/`
Contains various neural network models tested during experimentation. Includes training and evaluation code for alternative model architectures.

#### 🎯 `latin_hypercube_sampling.py`
Implements **Latin Hypercube Sampling (LHS)** to generate representative and diverse input distributions used for model training and validation.

---

### 🚀 Features
- Fast, low-latency performance prediction via reduced-order modeling
- Integrated web app for real-time input/output interaction
- Visual analysis tools for interpreting ROM behavior
- Support for experimentation with multiple ML architectures
- Built-in sampling strategies to optimize data generation

---
