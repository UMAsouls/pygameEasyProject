import os


for i in os.listdir("C:/Users/admin/pygameEasyProject/TestProject/object/default"):
    if(i[0] == "_" or i[0] == "."):
        continue
    exec(f"from object.default import {i}"[0:-3])


__all__ = [k[0:-3] for k in filter(lambda x: x[0] != "_" and x[0] != ".",
                    os.listdir(os.path.dirname(__file__)))]