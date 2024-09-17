# InvTrackr

**InvTrackr** is a Python tool for automating inventory management. It tracks stock levels, predicts stock-out events, and generates automatic reordering triggers.

## Features

- **Stock Tracking:** Monitors current stock levels and updates based on sales and restocks.
- **Stock-Out Prediction:** Uses time series analysis to predict potential stock-outs.
- **Reordering Triggers:** Automatically generates reorder notifications when stock levels are low.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- statsmodels
- numpy
- (Optional) SMTP server for email notifications

## Installation

```bash
pip install pandas scikit-learn statsmodels numpy
