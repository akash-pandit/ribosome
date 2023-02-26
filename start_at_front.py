from re import findall

codons = {
    "UUU": "Phe", "UCU": "Ser", "UAU": "Tyr", "UGU": "Cys",
    "UUC": "Phe", "UCC": "Ser", "UAC": "Tyr", "UGC": "Cys",
    "UUA": "Leu", "UCA": "Ser", "UAA": False, "UGA": False,
    "UUG": "Leu", "UCG": "Ser", "UAG": False, "UGG": "Trp",

    "CUU": "Leu", "CCU": "Pro", "CAU": "His", "CGU": "Arg",
    "CUC": "Leu", "CCC": "Pro", "CAC": "His", "CGC": "Arg",
    "CUA": "Leu", "CCA": "Pro", "CAA": "Gln", "CGA": "Arg",
    "CUG": "Leu", "CCG": "Pro", "CAG": "Gln", "CGG": "Arg",

    "AUU": "Ile", "ACU": "Thr", "AAU": "Asn", "AGU": "Ser",
    "AUC": "Ile", "ACC": "Thr", "AAC": "Asn", "AGC": "Ser",
    "AUA": "Ile", "ACA": "Thr", "AAA": "Lys", "AGA": "Arg",
    "AUG": "Met", "ACG": "Thr", "AAG": "Lys", "AGG": "Arg",

    "GUU": "Val", "GCU": "Ala", "GAU": "Asp", "GGU": "Gly",
    "GUC": "Val", "GCC": "Ala", "GAC": "Asp", "GGC": "Gly",
    "GUA": "Val", "GCA": "Ala", "GAA": "Glu", "GGA": "Gly",
    "GUG": "Val", "GCG": "Ala", "GAG": "Glu", "GGG": "Gly"
}

mRNA = input()
while mRNA.strip() != findall('[ACUG]+', mRNA)[0]:
    print('Invalid input, please provide a string solely composed of the characters A, G, C, or U as seen in mRNA.')
    mRNA = input()

mRNA = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]
print(mRNA)
polypeptides, polypeptide = [], []
terminated = True
for i in range(len(mRNA)):
    if mRNA[i] == 'AUG' and terminated:
        terminated = False
        polypeptide.append('Met')
    elif mRNA[i] is mRNA[-1] and codons[mRNA[i]]:
        polypeptides.append(polypeptide.copy())
        print('ALERT: The above polypeptide had no stop sequence, and terminated due to the end of the mRNA sequence.')
    elif polypeptide:
        if codons[mRNA[i]]:
            polypeptide.append(codons[mRNA[i]])
        else:
            terminated = True
            polypeptides.append(polypeptide.copy())
            polypeptide.clear()

for i in polypeptides:
    print('-'.join(i))
