# First Inference Plan

## Goal

Run a small open-source LLM directly with Hugging Face Transformers before introducing a serving engine such as vLLM.

The goal is to understand the basic inference path:

```text
Prompt
  -> Tokenizer
  -> Model
  -> GPU
  -> Generated tokens
  -> Decoded text
```
---

## Why start without vLLM

Starting with direct model inference helps clarify:

- how prompts become tokens
- how models are loaded into GPU memory
- why VRAM matters
- how generation parameters affect output
- what happens before production serving layers are introduced

---

## Model selection criteria

The first model should be:

- small enough to load quickly
- compatible with a 24GB GPU
- available on Hugging Face
- instruction-tuned
- useful for text generation

### Initial candidate

```text
Qwen/Qwen2.5-3B-Instruct
```

### Reasons

- small enough for fast experimentation
- strong quality for its size
- good documentation
- suitable for learning inference behavior

---

## Metrics to observe

For the first inference test, we will observe:

- model download size
- GPU memory before loading
- GPU memory after loading
- time to load the model
- generation latency
- output quality
- GPU utilization during generation

---

## Expected result

A successful first inference should produce:

- a generated answer from the model
- visible GPU memory usage in `nvidia-smi`
- a documented baseline for later comparison with vLLM