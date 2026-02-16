from mazegen import MazeGenerator

gen = MazeGenerator(width=10, height=6, seed=42)
gen.generate()
print(gen.grid)        # estrutura do labirinto
for i in range(20):
    print()
print(gen.solution)    # caminho solução