import warnings
warnings.filterwarnings(
    "ignore",
    message=".*urllib3 v2 only supports OpenSSL.*"
)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


MODEL_ID = "Qwen/Qwen1.5-0.5B-Chat"

def get_device() -> str:
    """
    自动选择可用设备：
    1. NVIDIA GPU：cuda
    2. Apple Silicon Mac：mps
    3. 普通 CPU：cpu
    """
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"

def load_model_and_tokenizer(model_id: str = MODEL_ID):
    """
    加载 Hugging Face 模型和分词器。
    """
    device = get_device()
    print(f"Using device: {device}")

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    if device == "cuda":
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            dtype=torch.float16
        ).to(device)
    elif device == "mps":
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            dtype=torch.float16
        ).to(device)
    else:
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            dtype=torch.float32
        ).to(device)

    model.eval()

    print("模型和分词器加载完成！")

    return model, tokenizer, device


if __name__ == "__main__":
    model, tokenizer, device = load_model_and_tokenizer()

