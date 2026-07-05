import torch

from tokenizer import CharTokenizer
from gpt import MiniGPT, GPTConfig


# Load training text
with open(
    r"data/iot_queries.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()


# Tokenizer
tokenizer = CharTokenizer(text)


# Config
config = GPTConfig(
    vocab_size=tokenizer.vocab_size,
    block_size=64,
    n_layer=4,
    n_head=4,
    n_embd=128
)


# Model
model = MiniGPT(config)

model.load_state_dict(
    torch.load(
        r"data/model.pt",
        map_location="cpu"
    )
)

model.eval()


def generate(
    prompt,
    max_new_tokens=100
):

    tokens = tokenizer.encode(prompt)

    idx = torch.tensor(
        [tokens],
        dtype=torch.long
    )

    for _ in range(max_new_tokens):

        idx_cond = idx[:, -64:]

        logits, _ = model(idx_cond)

        logits = logits[:, -1, :]

        probs = torch.softmax(
            logits,
            dim=-1
        )

        next_token = torch.multinomial(
            probs,
            num_samples=1
        )

        idx = torch.cat(
            [idx, next_token],
            dim=1
        )

    return tokenizer.decode(
        idx[0].tolist()
    )


prompt = input("Prompt: ")

result = generate(prompt)

print("\nGenerated:\n")
print(result)