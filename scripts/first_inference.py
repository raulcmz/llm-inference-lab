import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"


def main() -> None:
    print(f"Loading tokenizer: {MODEL_ID}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

    print(f"Loading model: {MODEL_ID}")
    start_load = time.perf_counter()

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    load_time = time.perf_counter() - start_load
    print(f"Model loaded in {load_time:.2f} seconds")

    prompt = "Explain what KV cache is in LLM inference in simple terms."

    messages = [
        {"role": "system", "content": "You are a helpful technical assistant."},
        {"role": "user", "content": prompt},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer([text], return_tensors="pt").to(model.device)

    print("Running generation...")
    start_generation = time.perf_counter()

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False,
    )

    generation_time = time.perf_counter() - start_generation

    generated_ids = outputs[0][inputs.input_ids.shape[-1]:]
    response = tokenizer.decode(generated_ids, skip_special_tokens=True)

    print("\n--- Response ---")
    print(response)
    print("\n--- Metrics ---")
    print(f"Load time: {load_time:.2f}s")
    print(f"Generation time: {generation_time:.2f}s")
    print(f"Generated tokens: {len(generated_ids)}")
    print(f"Tokens/sec: {len(generated_ids) / generation_time:.2f}")


if __name__ == "__main__":
    main()