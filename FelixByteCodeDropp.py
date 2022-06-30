from ghidra.app.util.exporter import BinaryExporter
from ghidra.program.model.address import AddressSet
from binascii import hexlify

def dump_raw_bcode(func):
	str=""
	addrSet = func.getBody()
    	codeUnits = listing.getCodeUnits(addrSet, True) # true means 'forward'
	for codeUnit in codeUnits:
		str = str + "{}\n".format(hexlify(codeUnit.getBytes()))
	return str


listing = currentProgram.getListing()
func = getFunctionContaining(currentAddress)

if func is None:
	println("No Function at address " + str(currentAddress))
	exit(1)

path = "/home/felix/ghidra_scripts/bytecode_dump/bin_dump_"+currentProgram.getName()+"_"+func.getName()

with open(path, "w") as out_f:
	out_f.write(dump_raw_bcode(func))

with open(path, "r") as in_f:
    	print(in_f)
    	print(in_f.readlines())




