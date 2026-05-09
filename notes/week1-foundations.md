# Week 1 — Foundations

## Project goal

This project is a hands-on LLM inference lab focused on understanding and measuring open-source LLM serving.

The goal is to learn and document:

- GPU runtime validation
- CUDA and NVIDIA driver basics
- remote GPU access with SSH
- containerized inference environments
- vLLM serving
- latency metrics such as TTFT and TPOT
- throughput benchmarking
- basic MLOps/LLMOps observability

## Why this project matters

This project connects DevOps experience with MLOps/LLMOps skills.

Instead of only consuming external APIs, the goal is to deploy, operate, benchmark, and explain an LLM inference stack.

## Local vs remote workflow

The GitHub repository is managed from the local Ubuntu VM.

The Vast.ai GPU instance is used only for GPU-heavy execution such as:

- validating GPU availability
- running vLLM
- executing benchmarks
- collecting metrics

This avoids storing GitHub credentials or long-lived secrets on the remote GPU instance.

## Infrastructure decision

A remote RTX 3090 GPU instance was selected because:

- 24GB VRAM is enough for small and medium open-source LLM inference experiments
- it is cost-effective
- it supports CUDA workloads
- it is suitable for learning serving, benchmarking, and latency trade-offs

## Lessons learned so far

### Template vs instance

A template defines the software environment.

An instance defines the hardware resources such as GPU, VRAM, CPU, RAM, disk, and networking.

### VRAM vs disk

GPU VRAM is used for:

- model weights
- KV cache
- inference execution
- concurrent requests

Container disk is used for:

- model downloads
- Python packages
- logs
- benchmark outputs
- documentation artifacts

### Host resources vs allocated resources

The physical host may have much more disk than the container allocation.

The project initially exposed this difference when a 16GB container disk was not enough for LLM workloads.

### SSH workflow

SSH is used to access the remote GPU instance from the local Ubuntu VM.

This is closer to real MLOps workflows than working only through notebooks.

### tmux

Vast.ai starts sessions inside tmux.

tmux allows processes to keep running even if the SSH connection drops.

### GPU validation

The environment was validated with `nvidia-smi`, confirming:

- NVIDIA RTX 3090 detected
- 24GB VRAM available
- CUDA runtime available
- no active GPU workloads before starting inference