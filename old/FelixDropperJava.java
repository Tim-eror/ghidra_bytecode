//TODO write a description for this script
//@author Felix Schaefer
//@category _NEW_
//@keybinding 
//@menupath 
//@toolbar 

import ghidra.app.script.GhidraScript;
import ghidra.program.model.mem.*;
import ghidra.program.model.lang.*;
import ghidra.program.model.pcode.*;
import ghidra.program.model.util.*;
import ghidra.program.model.reloc.*;
import ghidra.program.model.data.*;
import ghidra.program.model.block.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.scalar.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.address.*;
import ghidra.app.util.exporter;

public class FelixDropperJava extends GhidraScript {

    public void run() throws Exception {
    	AddressSet asv =  new AddressSet();
	BinaryExporter exporter = new BinaryExporter();

	//for f in currentProgram.getFunctionManager().getFunctions(True):
	Function func = getFunctionContaining(currentAddress);
	if (func==null){
		println("No Function at address " + currentAddress);
		return;
	}

	asv.add(func.getBody());

	String out = "/home/felix/ghidra_scripts/target_file.bin";


    }

}
