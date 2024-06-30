import os


for i in os.listdir(os.path.dirname(__file__)):
    if(i[0] == "_" or i[0] == "."):
        continue
    exec(f"from object.shooting import {i}"[0:-3])


__all__ = [k[0:-3] for k in filter(lambda x: x[0] != "_" and x[0] != ".",
                    os.listdir(os.path.dirname(__file__)))]