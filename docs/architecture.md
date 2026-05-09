# LLM Inference Lab — Architecture

## High-Level Overview

The project uses a hybrid local/remote workflow.

Local machine responsibilities:
- source code management
- Git operations
- documentation
- benchmark analysis
- experiment orchestration

Remote GPU instance responsibilities:
- model execution
- GPU inference
- vLLM serving
- benchmark runtime
- latency measurements

---

## Architecture Diagram

```text
+----------------------+
| Local Ubuntu VM      |
|----------------------|
| VS Code              |
| Git/GitHub           |
| Python venv          |
| Documentation        |
| Analysis             |
+----------+-----------+
           |
           | SSH
           |
+----------v-----------+
| Vast.ai GPU Instance |
|----------------------|
| RTX 3090             |
| CUDA                 |
| PyTorch              |
| vLLM                 |
| OpenAI API server    |
| Benchmark runtime    |
+----------------------+
```

## Why This Architecture

This separation provides:

- lower cloud costs
- safer credential management
- reproducibility
- cleaner workflows
- realistic infrastructure practices

---

## Inference Workflow

Typical workflow:

1. Prepare code locally
2. Commit and push changes
3. Start GPU instance only when needed
4. Pull latest repository changes remotely
5. Execute inference or benchmarks
6. Save metrics/results
7. Push results back to GitHub
8. Stop GPU instance

---

## Cost Optimization Strategy

The GPU instance should remain stopped unless actively:

- running inference
- downloading models
- benchmarking
- validating runtime behavior

This minimizes unnecessary GPU costs.

---

## Planned Runtime Stack

Local

- Ubuntu
- VS Code
- Python 3.12
- Git

Remote

- CUDA 13
- NVIDIA RTX 3090
- PyTorch
- vLLM
- Hugging Face ecosystem

## Future Extensions

Potential future improvements:

- Prometheus metrics
- Grafana dashboards
- multi-model serving
- quantized inference
- Docker Compose orchestration
- Kubernetes deployment
- distributed inference