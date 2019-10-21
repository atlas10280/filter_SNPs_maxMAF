# script parse vcf file get alleles per individual
import os

os.getcwd()
os.chdir("I:/WAE_RAD_Data/novoseq2/STACKS/Filter_steps/genomics")
# open vcf file read all lines into an array, close file
raw_vcf_file = open("v5_novoseq2_snps.recode.vcf", "r")
raw_vcf_array = raw_vcf_file.readlines()
raw_vcf_file.close()

# open file you are going to write new results to
out_file = open("v6_novoseq2_allele_freq_info.txt", "w")
r = 1

# for each line in vcf file
for i in raw_vcf_array:
    # this is trying to recognize the header line
    if i.startswith("#CHROM"):

        # hard code column names you wan
            out_file.write(
            "Chrom" + "\t" + "Position" + "\t" + "REF1" + "\t" + "REF2" + "\t" + "Minor_Allele_Frequency")
            header_line = i.rstrip().split("\t")
            # grabbing individual names
            #z = 0
            #for j in header_line:
                #z = z + 1                
                #if z > 9 and z < len(header_line)+1:
                    #out_file.write(j + "\t")                 
                #else: out_file.write(j)

            out_file.write("\n")
            # at this point we should have header line

    # use the if not # to go to the data
    elif "#" not in i:
        # splits each thing into their respective cells by tabs
        split_ind_line = i.rstrip().split("\t")
        
        # outputs locus name, you're going to need to output stuff from other columns to
        out_file.write(split_ind_line[0] + "\t" + split_ind_line[1] + "\t" + split_ind_line[3] + "\t" + split_ind_line[4] + "\t")
        
        # iterates through individuals
        z = 0
        A1 = 0
        A2 = 0

        for j in split_ind_line:
            #print j
            z = z + 1
            #print z
            if z > 9:
                # split the genotype cell
                gen_data = j.split(":")

                # print out the genotype
                
                allele_data = gen_data[0].split("/")
                if allele_data[0] != '.':
                    
                    if allele_data[0] == '0':
                        A1 = A1+1
                    if allele_data[1] == '0':
                        A1 = A1+1
                    if allele_data[0] == '1':
                        A2 = A2 +1
                    if allele_data[1] == '1':
                        A2 = A2 +1
        if A1 < A2:
            minor_allele_freq = A1/(A1+A2)
        if A2 < A1:
            minor_allele_freq = A2/(A2+A1)
        if A1 == A2:
            minor_allele_freq = 0.5
        minor_allele_freq = str(minor_allele_freq)
        out_file.write(minor_allele_freq)



        out_file.write("\n")


out_file.close()  # script parse vcf file get alleles per individual
