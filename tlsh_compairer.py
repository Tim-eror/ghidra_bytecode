import tlsh
h1 = tlsh.hash(open("bytecode_dump/bin_dump_tcp_sever__print", 'rb').read())
h2 = tlsh.hash(open("bytecode_dump/bin_dump_tcp_relase__print", 'rb').read())
score = tlsh.diffxlen(h1, h2)
print(score)
print(h1)
print(h2)

import ssdeep
h1 = ssdeep.hash(open("bytecode_dump/bin_dump_tcp_sever__print", 'rb').read())
h2 = ssdeep.hash(open("bytecode_dump/bin_dump_tcp_relase__print", 'rb').read())
score = ssdeep.compare(h1, h2)
print(score)
print(h1)
print(h2)
