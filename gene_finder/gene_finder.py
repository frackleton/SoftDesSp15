# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Mackenzie Frackleton

"""
#print "###########################################################"
# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
dna=load_seq("./data/X73525.fa")
def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    elif nucleotide == 'T':
        return 'A'

   
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    reverse_complement=[]
    for base in range(len(dna)-1, -1, -1): # calling index, not letter
        reverse_complement.append(get_complement(dna[base]))
    return ''.join(reverse_complement) 

    
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    
    ORF= []
    for i in range (0, len(dna),3):
        codon = dna[i:i+3]
        if codon == 'TGA' or codon == 'TAG' or codon =='TAA':
            break 
#       elif len(codon)<3:
#            break
        else:
            ORF.append(codon)      
    #print ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ", ORF    
    return ''.join(ORF)

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """

    count=0
    ORF=[]
    for i in range(0,len(dna),3):
        codon = dna[i:i+3]
        if codon=='ATG':
            dna=dna[i:]
            ORF.insert(count,rest_of_ORF(dna))
            dna=dna[len(rest_of_ORF(dna)):]
            count+=1
    return ORF

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    ORFs=[]
    for i in range(3):
        ORFs.extend(find_all_ORFs_oneframe(dna[i:]))
    
    return ORFs
    
    

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    ORFb=[]
    ORFb.extend(find_all_ORFs(dna))
    ORFb.extend(find_all_ORFs(get_reverse_complement(dna)))
    return ORFb


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    longest_ORF=''
    sample=find_all_ORFs_both_strands(dna)#just takes the output list 
    for component in sample: #component is each str in the list
        if len(component) > len(longest_ORF):
            longest_ORF = component
    return longest_ORF



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
#added in a makeshift test where I ran it with different lengths of code after I imported it in terminal. For example:
#longest_ORF_noncoding("ATGCGAATGTAGCATCAAA",5) and then varied lengths of base strings and different numbers of trials
#I realized that the ratio of string length:number of trials will give me a different length noncoding ORF
#I needed an ORF sufficiently shorter than the whole dna sample, so that's what I ended up looking for
#ran wc on the dna input and the function's output; if the out put was shorter enough it was good. 
    longest_ORF_noncoding=''
    for i in range(num_trials):
        sample=longest_ORF(shuffle_string(dna))#just takes the output list 
        if len(sample) > len(longest_ORF_noncoding):
            longest_ORF_noncoding = sample
    return len(longest_ORF_noncoding)
#
#This outputs(essentially) the length of the dna strand, but gene_finder looks for a component of the dna strand that is longer than the whole. why? 


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    #plan: search codons for the index of the list containing the triplet
    #take that index number, and append to the list the appropriate corresponding letter
    amino_acid=''
    for i in range (0, len(dna),3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            amino_acid += aa_table[codon]
    return amino_acid

def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
#pulled apart and ran multiple times, consistently got the same amino acid output 

    sequence=[]
    minimum = longest_ORF_noncoding(dna,1500) #if a strand has a length longer than this, it is probably coding. 
    ORF_list = find_all_ORFs_both_strands(dna)#put dna into find all orf both
    for component in ORF_list:
        if len(component) > minimum: #compare the results of the above to lenminimum
            sequence.append(coding_strand_to_AA(component)) #if longer than minimum, plug into coding_strand_to_AA
    return ''.join(sequence)
print gene_finder(dna)
if __name__ == "__main__":
    import doctest
    doctest.testmod()