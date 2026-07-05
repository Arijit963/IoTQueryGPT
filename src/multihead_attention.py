import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):

    def __init__(self, embed_dim, num_heads):

        super().__init__()

        assert embed_dim % num_heads == 0

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.Wq = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wk = nn.Linear(embed_dim, embed_dim, bias=False)
        self.Wv = nn.Linear(embed_dim, embed_dim, bias=False)

        self.proj = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):

        B, T, C = x.shape

        q = self.Wq(x)
        k = self.Wk(x)
        v = self.Wv(x)

        # Split heads
        q = q.view(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(1, 2)

        k = k.view(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(1, 2)

        v = v.view(
            B,
            T,
            self.num_heads,
            self.head_dim
        ).transpose(1, 2)

        scores = (
            q @ k.transpose(-2, -1)
        ) / math.sqrt(self.head_dim)

        mask = torch.tril(
            torch.ones(
                T,
                T,
                device=x.device
            )
        )

        scores = scores.masked_fill(
            mask == 0,
            float("-inf")
        )

        att = F.softmax(scores, dim=-1)

        out = att @ v

        out = (
            out.transpose(1, 2)
               .contiguous()
               .view(B, T, C)
        )

        out = self.proj(out)

        return out
    
    
if __name__ == "__main__":

    x = torch.randn(2, 4, 8)

    mha = MultiHeadAttention(
        embed_dim=8,
        num_heads=2
    )

    out = mha(x)

    print(out.shape)