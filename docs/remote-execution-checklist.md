# Remote Execution Checklist

## Goal

Run the first direct LLM inference on a remote GPU instance in a controlled and documented way.

## Pre-flight checklist

Before starting the GPU instance:

- [ ] local repository is committed and pushed
- [ ] GPU instance is stopped
- [ ] estimated execution window is planned
- [ ] Hugging Face access token is available if required
- [ ] remote SSH command is available
- [ ] expected screenshots are defined

## Remote validation steps

Once connected to the GPU instance:

1. Validate GPU availability

```bash
nvidia-smi
```

2. Validate working directory and storage

```bash
pwd
df -h
```

3. Clone or update the project repository

```bash
git clone <repo-url>
```

or:

```bash
git pull
```

4. Create Python environment if needed

```bash
python -m venv .venv
source .venv/bin/activate
```

5. Install GPU dependencies

```bash
pip install -r requirements-gpu.txt
```

6. Run first inference

```bash
python scripts/first_inference.py
```

7. Capture results

Observe:

- model loading time
- GPU memory usage
- generation latency
- tokens per second
- generated response quality

8. Stop the GPU instance after the experiment


---

## Screenshots


- Vast.ai running instance with GPU and cost
- nvidia-smi before model loading
- nvidia-smi after model loading
- first successful inference output
- terminal output showing basic metrics

---

## Success criteria

The experiment is successful when:

- the model loads on GPU
- inference produces a valid response
- GPU memory usage is visible
- first latency and throughput metrics are recorded
- results are documented locally
