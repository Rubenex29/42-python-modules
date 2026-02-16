# mazegen

Single-file maze generator module with a built-in solver.

## Install (local build)

```bash
python -m pip install --upgrade build
python -m build
python -m pip install dist/mazegen-1.0.0-py3-none-any.whl
```

## Usage

```python
from mazegen import MazeGenerator

gen = MazeGenerator(width=10, height=6, seed=42)
gen.generate()

print(gen.entry, gen.exit)
print(gen.solution)
print("\n".join(gen.to_hex_lines()))
```

## Parameters

- `width`, `height`: maze size
- `seed`: random seed for reproducibility
- `entry`, `exit`: custom start/end coordinates
