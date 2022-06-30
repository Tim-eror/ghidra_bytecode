with open("target_file.bin", "w") as out_f:
    out_f.write("contend")
#ret = exporter.export(file, currentProgram, asv, monitor)


with open("target_file.bin", "r") as in_f:
    print(in_f)
    print(in_f.readlines())
