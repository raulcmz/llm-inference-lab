# LLM Inference Lab — Roadmap

## Phase 1 — Foundations

Goal:
Understand the infrastructure and runtime environment.

Topics:
- Vast.ai workflows
- SSH access
- GPU validation
- CUDA basics
- VRAM concepts
- tmux sessions
- remote Linux workflows

Deliverables:
- working remote GPU instance
- validated NVIDIA runtime
- documented setup process

Status:
- [x] completed

---

## Phase 2 — Environment Preparation

Goal:
Prepare a reproducible inference environment.

Topics:
- Python environments
- package management
- Hugging Face ecosystem
- model storage
- container persistence

Deliverables:
- reproducible setup scripts
- dependency documentation
- environment validation

Status:
- [ ] pending

---

## Phase 3 — First LLM Inference

Goal:
Run a local open-source LLM.

Topics:
- tokenizer basics
- prompt formatting
- inference pipeline
- model loading
- GPU memory usage

Deliverables:
- first successful generation
- VRAM measurements
- inference notes

Status:
- [ ] pending

---

## Phase 4 — vLLM Serving

Goal:
Deploy production-style inference serving.

Topics:
- vLLM architecture
- continuous batching
- OpenAI-compatible APIs
- KV cache
- throughput optimization

Deliverables:
- running vLLM server
- API endpoint
- latency measurements

Status:
- [ ] pending

---

## Phase 5 — Benchmarking

Goal:
Measure inference performance scientifically.

Topics:
- TTFT
- TPOT
- throughput
- concurrency
- batch size effects

Deliverables:
- benchmark scripts
- benchmark reports
- charts and analysis

Status:
- [ ] pending

---
