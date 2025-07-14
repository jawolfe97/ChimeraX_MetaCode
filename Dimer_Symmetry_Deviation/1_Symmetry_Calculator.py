Path = "C:/Users/jawol/OneDrive/Desktop/Horne Lab Work/Raw Data/MID1-Zinc/X-Ray/Symmetry Analysis/3V1C_3V1D"
PDB = "3V1B"
Atom = "Ca"

output_filename = "SymmetryValues"

subunits = ["A","B"] #Must be two in dimer
start_res = [4,26] #Starting residue of the first and second stretch of protein, more can be added. Must equal length of end res
end_res = [23,46] #Ending residue of the first and second stretch of protein, more can be added. Must equal length of end res
res_list = [n for i in range(len(start_res)) for n in range(start_res[i], end_res[i] + 1)] #List off all positions

with open(f"Symmetry_Calculator_{PDB}.cxc", "w") as file:
    file.write(f'cd "{Path}";\nselect;\n~show;\n~ribbon;\n~select;log clear;\nopen {PDB};\n')
    for i in range(len(res_list)):
        for j in range(i + 1, len(res_list)):
            file.write(f"rmsd #1/{subunits[0]}:{res_list[i]}@{Atom} to #1/{subunits[1]}:{res_list[j]}@{Atom};\n")
            file.write(f"rmsd #1/{subunits[1]}:{res_list[i]}@{Atom} to #1/{subunits[0]}:{res_list[j]}@{Atom};\n")
    file.write(f'log save {PDB}_{Atom}_{output_filename}_InterDistances.txt; log clear; close all;\n')
