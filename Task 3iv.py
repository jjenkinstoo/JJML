from __future__ import division

primary = ""
with open(r"C:\Users\Matthew\Documents\Northwestern\Bio 323\Homework\5\contig2protein.txt", "r") as infile:
	header = infile.readline()
	for line in infile:
		sline = line[:-1]
		primary = primary + sline
		
def composition(protein):
	seqlen = len(protein)
	
	#Make a dictionary (residuecount) where the keys are the residues and the values are 0, 
	#because we're gonna use a for loop later to add 1 for each instance of the residues
	residuecount = {
		"A":0, 
		"C":0, 
		"D":0, 
		"E":0, 
		"F":0, 
		"G":0, 
		"H":0, 
		"I":0, 
		"K":0, 
		"L":0, 
		"M":0, 
		"N":0, 
		"P":0, 
		"Q":0, 
		"R":0, 
		"S":0, 
		"T":0, 
		"V":0, 
		"W":0, 
		"Y":0
	}
	
	#Also make a dictionary (labels) with the SAME KEYS AS THE COUNTING DICTIONARY with the 
	#labels that will be used to tie everything else together at the end
	labels = {
		"A":"Ala (A)", 
		"C":"Cys (C)", 
		"D":"Asp (D)", 
		"E":"Glu (E)", 
		"F":"Phe (F)", 
		"G":"Gly (G)", 
		"H":"His (H)", 
		"I":"Ile (I)", 
		"K":"Lys (K)", 
		"L":"Leu (L)", 
		"M":"Met (M)", 
		"N":"Asn (N)", 
		"P":"Pro (P)", 
		"Q":"Gln (Q)", 
		"R":"Arg (R)", 
		"S":"Ser (S)", 
		"T":"Thr (T)", 
		"V":"Val (V)", 
		"W":"Trp (W)", 
		"Y":"Tyr (Y)"
	}

	#For loop to count the residues in the protein and add the counts to the residuecount
	#dictionary
	for residue in protein:
		residuecount[residue] += 1

	#Take the counts in the dictionary and make a new dictionary (respercent) to hold the 
	#percentages
	respercent = {}	
	for residue in residuecount:
		respercent[residue] = residuecount[residue] * 100 / seqlen

	#Save the keys of the count dictionary in a list (alphabetical) then sort that list 
	#(necessary because because dictionaries are unsorted)
	alphabetical = residuecount.keys()
	alphabetical.sort()
	
	with open(r"C:\Users\Matthew\Documents\Northwestern\Bio 323\Homework\5\composition.txt", "w") as outfile:
		#Put everything together, write the for loop for alphabetical (list) because it's been
		#sorted. In the body of the loop, call the dictionaries. This will only work because the
		#items in the list are the same as the keys of the dictionaries (which was by design)
		for label in alphabetical:
			outfile.write(labels[label] + ("%3d" % residuecount[label]) + ("%5.1f" % respercent[label]) + "%" + "\n")

composition(primary)