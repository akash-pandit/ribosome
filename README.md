# Ribosome
### Explanation:
With either file, a valid mRNA sequence should be given from its 5' to 3' end, as how a ribosome would normally read a molecule
of mRNA. Given that, it will output a chain of amino acids concatenated together by hyphens, and represented with their common 
3 letter abbreviations. These are all the amino acid chains or polypeptides that would be coded by the given mRNA sequence assuming
all untranslated regions (UTRs) are left out.

The main difference between start_at_front.py and start_at_AUG.py is how they determine where to start. 'start_at_front.py' 
treats the whole nucleotide sequence as a set of codons, and splits the sequence into codons from the very beginning, then checks
codons until it finds the start (AUG) sequence. 

'start_at_AUG.py' functions differently, finding the first occurrence of the pattern 'AUG', then splitting the remainder of the
mRNA string into their respective codons.

By simply changing when the 'ribosome' begins reading, the polypeptide output can vary wildly, where a sequence 'AAUGGGG' could either
be split as ['AAU', 'GGG', 'A'], which produces nothing, or ['AUG', 'GGA'], which produces a chain 'Met-Asn', or methionine and asparagine.

### Background: 
Ribosomes are an organelle that translate mRNA sequences made of nucleotides with Adenine (A), Uracil (U), Cytosine (C), and Guanine (G).

These chains of nucleotides are read in sets of 3, called codons. Each codon represents an amino acid, a start sequence (AUG), or a stop sequence.

Start sequences are called promoters, and is where RNA first begins its transcription.
Following codons are read after, each one adding a new amino acid to the growing polypeptide chain until a stop codon is reached,
and the newly formed protein detaches from the ribosome. 

The ribosome can continue reading and if another AUG sequence is detected, a new polypeptide will begin to be built.

This process is how all of us build every single protein in our bodies, and these 2 programs simulate that process.

### Method

In both files, the mRNA input is checked to see if it's a valid input, comprised solely of A, C, U, or G. If not, the user is
prompted to provide a proper input with explanation of what that is until they do.

In start_at_front.py, the validated mRNA is then split by list comprehension into a list of codons, units of characters 3 letters long.

In start_at_AUG.py, the search function from Python's regular expression builtin module is used to find the first occurrence of the
start codon 'AUG', then sections off AUG and the remaining string as the new nucleotide sequence and splits it as in start_at_front.py


In both files, variables for a single polypeptide, a list of polypeptides, and whether translation is terminated or not are initialized.
The list of codons is then iterated through.

First, codons are iterated over until the start sequence, AUG, is found. The termination variable is set to False, and
its associated amino acid, Met (methionine), is added to the list of peptides.

For each following codon until a stop sequence, a dictionary version of a codon chart is referenced to add each successive amino
acid to the growing peptide chain. Once a stop codon is encountered, the termination variable is set to True and no new amino
acids may be added to the polypeptide.

The resulting polypeptide variable is copied and emptied, with that copy added to the list of polypeptides.

The cycle repeats as long as there are codons left to iterate over, with new start sequences signalling the creation of new 
polypeptides.

If the last codon is reached and translated with no stop sequence, a warning is given with the polypeptide chain that there was
no stop codon.
