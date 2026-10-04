# groundup

Everything ML and AI, built from the ground up.

This repo is my learning log: I rebuild core ML ideas from scratch (following Andrej Karpathy's *Neural Networks: Zero to Hero*), build up the math underneath them, and wire some of it into a small full-stack app.

## What's done so far

### Neural networks from scratch (`karpathy/`)

| Folder | What I built |
| --- | --- |
| `micrograd/` | A tiny autograd engine: a `Value` class that tracks the computation graph and does backpropagation by hand. It supports `+`, `*`, `tanh` and more, with gradients checked against numerical derivatives. |
| `makemore_pt1/` | A character-level **bigram language model** on a names dataset. I did it two ways: counting bigrams into a 27x27 probability table, and learning the same table with random weights and gradient descent. Then I sampled new names from it. |
| `makemore_pt2_mlp/` | An **MLP language model** (Bengio et al. style): character embeddings, a context window of 3, a hidden layer, and a softmax output. Includes a train/dev/test split and minibatch training. |
| `makemore_pt3_gradients/` | Work in progress on the training internals: dataset building and the train/dev/test split, as setup for activations, gradients and BatchNorm. |

Each folder has a `*_learning.ipynb` (following along with the lecture) and, where applicable, a cleaned-up version I wrote on my own.

### Math (`math/`)

- **`linear_algebra/`** has vectors, linear independence, span, and 2D transformations (rotation and shear). The reusable code is in `linear_algebra.py` (`check_dependent`, `rotate_clockwise`, `rotate_counterclockwise`, `shear`, `plot_span`), and the walkthrough is in `linear_algebra.ipynb`.
- `calculus/` and `statistics/` are planned.

### Small full-stack app (`backend/` + `frontend/`)

A React + Vite frontend that sends vectors to a FastAPI backend. The backend calls my own `check_dependent` function and returns whether the vectors are linearly dependent. It shows how the math code can be served as an API.

## Running it

```bash
# setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# notebooks
jupyter lab            # open anything under karpathy/ or math/

# backend (http://localhost:8000)
cd backend && fastapi dev main.py

# frontend (http://localhost:5173)
cd frontend && npm install && npm run dev
```

## Stack

Python, PyTorch, NumPy, Matplotlib, Graphviz, FastAPI, React, Vite.

## Next up

Finish the makemore series (BatchNorm, manual backprop, WaveNet), then GPT from scratch, plus calculus and statistics.
