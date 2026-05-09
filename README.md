# LLM Inference Lab

Hands-on laboratory for learning modern LLM inference, GPU serving, benchmarking, and LLMOps fundamentals using open-source models.

## Goals

This project focuses on understanding how production-style LLM inference works beyond simple API usage.

Main objectives:

- Learn GPU-based inference workflows
- Understand CUDA, VRAM, and model serving
- Deploy open-source LLMs with vLLM
- Benchmark latency and throughput
- Analyze TTFT and TPOT metrics
- Explore real-world LLMOps practices

---

## Tech Stack

### Infrastructure

- Vast.ai
- NVIDIA RTX 3090
- Ubuntu Linux
- SSH remote workflows

### AI / ML

- PyTorch
- Transformers
- vLLM
- Hugging Face

### Tooling

- Python 3.12
- Git & GitHub
- VS Code
- tmux

---

## Planned Experiments

- GPU environment validation
- Local vs remote inference comparison
- vLLM deployment
- Quantized model serving
- Batch inference benchmarking
- Concurrent request benchmarking
- VRAM usage analysis
- Token latency measurements
- Throughput optimization

---

## Repository Structure

```text
.
├── notes/          # Learning notes and explanations
├── results/        # Benchmark outputs and experiment artifacts
├── scripts/        # Automation and utility scripts
├── benchmarks/     # Benchmark configurations and tests
├── docs/           # Documentation and screenshots
└── README.md
```

## Learning Philosophy

This repository is intentionally educational.

The goal is not only to make things work, but to deeply understand:

- what is happening
- why it works
- how to debug it
- how to measure it
- how to explain it professionally

---

## Current Status

- ✅ GitHub repository created
- ✅ Vast.ai environment validated
- ✅ GPU runtime verified with nvidia-smi
- 🔜 vLLM deployment
- 🔜 First inference
- 🔜 Benchmark suite
- 🔜 Observability and metrics