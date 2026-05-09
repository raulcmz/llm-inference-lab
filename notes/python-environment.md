# Python Environment Notes

## Why virtual environments matter

Python virtual environments isolate dependencies per project.

Benefits:
- reproducibility
- dependency isolation
- easier debugging
- safer upgrades
- cleaner development workflows

## Why requirements.txt matters

requirements.txt documents the dependencies needed to reproduce the project environment.

This is critical for:
- collaboration
- deployment
- CI/CD
- cloud execution
- long-term maintainability

## Planned core dependencies

### torch

PyTorch framework used for tensor computation and GPU execution.

### transformers

Hugging Face library for loading pretrained LLMs and tokenizers.

### accelerate

Utility layer for efficient model execution.

### huggingface_hub

Allows downloading and managing models from Hugging Face.

### vllm

High-performance LLM serving engine optimized for throughput and latency.

### jupyter

Interactive notebook environment.

### matplotlib

Visualization library for charts and benchmark plots.

### pandas

Data analysis and benchmarking results processing.

### numpy

Numerical computation library used across the ML ecosystem.