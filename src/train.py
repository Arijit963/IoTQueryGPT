import torch
import torch.optim as optim

from tokenizer import CharTokenizer
from dataset import IoTDataset
from gpt import MiniGPT, GPTConfig


# Load dataset
with open(
    r"data/iot_queries.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

print("Dataset Length:", len(text))

# Tokenizer
tokenizer = CharTokenizer(text)

print("Vocabulary Size:", tokenizer.vocab_size)

# Dataset
dataset = IoTDataset(
    text,
    tokenizer,
    block_size=64
)
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Using Device:", device)


# Model Config
config = GPTConfig(
    vocab_size=tokenizer.vocab_size,
    block_size=64,
    n_layer=4,
    n_head=4,
    n_embd=128
)


# Model
model = MiniGPT(config).to(device)

print(
    "Parameters:",
    sum(
        p.numel()
        for p in model.parameters()
    )
)


# Optimizer
optimizer = optim.AdamW(
    model.parameters(),
    lr=3e-4
)


# Training Loop
for step in range(500):

    xb, yb = dataset.get_batch(
        batch_size=16
    )

    xb = xb.to(device)
    yb = yb.to(device)

    logits, loss = model(
        xb,
        yb
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    if step % 50 == 0:

        print(
            f"Step {step} | Loss {loss.item():.4f}"
        )

# Save model
torch.save(
    model.state_dict(),
    r"data/model.pt"
)

print("\nModel Saved Successfully!")
