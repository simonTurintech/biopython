from Bio.PDB import MMCIFParser

parser = MMCIFParser()
for i in range(100):
    structure = parser.get_structure("PHA-L", "1fat.cif")
