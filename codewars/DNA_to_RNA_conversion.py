def dna_to_rna(dna):
    """ "GCAT"  =>  "GCAU" """
    # return dna.replace("T", "U")
    rna = ""
    for letter in dna:
        if letter == "T":
            rna += "U"
        else:
            rna += letter
    return rna

    
