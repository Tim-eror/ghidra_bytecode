from difflib import diff_bytes
from os import listdir
import os.path

#Working similaly to diff -y bin_dump_helloStriped_FUN_00118890 bin_dump_tcp_sever__print

array={}

file_a = "bytecode_dump/bin_dump_tcp_sever_rust_panic"
file_diff = "diff_print"

a = open(file_a).read()
diff = open(file_diff).read()
str1=""
str2=""

for i in range(min(len(diff),len(a))):
    if diff[i] != "*":
        str1+= a[i]
        str2+= diff[i]

print(str1)
print(str2)

import ssdeep
h1 = ssdeep.hash(str1)
h2 = ssdeep.hash(str2)
score = ssdeep.compare(h1, h2)
print(score)
print(h1)
print(h2)

