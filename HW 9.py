#1.
def get_tsv_records(input_file):
    
    import os
    labels = []
    records = []
    with open(input_file) as instream:
        for line in instream:
            line = line.strip(os.linesep)
            record = line.split('\t')
            if len(labels) == 0:
                labels = record
            else:
                records.append(record)

    return(labels,records)
    

def write_records_to_tsv(labels,records,outfile):
    with open(outfile,'w') as outstream:
        outstring = ''
        
        for label in labels:
            outstring = outstring+label+'\t'
        outstring = outstring.strip('\t')
        outstring = outstring+'\n'
        outstream.write(outstring)
        for groups in records:

            for record in groups:
                outstring = ''
                outstring = outstring+record+'\t'
                outstream.write(outstring)
            outstring=''
            outstring = outstring+'\n'
            outstream.write(outstring)
            
            
            
def user_input_make_bw_phonebook():
    inputname=input("What input name do you want?")

    outputname=input("What output name do you want?")

    return(inputname,outputname)



def make_backwards_phonebook():
    #I choose the phone_numbers2.tsv as the input file
    inputname,outputname=user_input_make_bw_phonebook()
    labels,records= get_tsv_records(inputname)
    

    
    phonebook=dict()
    
    for i in records:
        phonebook[i[0]] =i[1]

    inv_phonebook=dict()
    for i in records:
        inv_phonebook[i[1]]=i[0]
    print(inv_phonebook)
    for i in records:
        i.reverse()
    labels.reverse()
    write_records_to_tsv(labels,records,outputname)
    
make_backwards_phonebook()
    
#2.

def holiday_convert_to_days(input_string):

    h_to_d={"easter":"04/01/2018",
            "chanukah":"12/02/2018",
            
            "christmas":"12/25/2018",
            "halloween":"10/31/2018",
            "thanksgiving":"11/22/2018",
            "kwanzaa":"12/26/2018",
            "ramadan":"05/16/2018",
            "passover":"03/20/2018"}

    
    
    list0= input_string.split(" ")
    

    empty_string=''
    for i in list0:
        i = i.strip(",").strip(".")
        
        for key,value in h_to_d.items():
            if key==i.lower():
                i=value
        empty_string += i
        empty_string += " "           
            
                

    
    print(empty_string)
            


    
    

#3.


def read_file(input_file):


    
    import os
    
    records = []
    with open(input_file) as instream:
        
        for line in instream:
            
            line = line.strip(os.linesep)
            
            record = line.split(' ')

            records.append(record)

    return(records)




def count_word_frequency(inputfile,outputfile):

    info= read_file(inputfile)
    with open(outputfile,'w') as outstream:
        

        flatlist=[]
        for i in info:
            for word in i:
                word = word.lower().strip(",").strip(".").strip("(").strip(")").strip('"')
                flatlist.append(word)
        flatlist.sort()
        print(flatlist)
        words=dict()
        
        for word in flatlist:
            freq=0
            
            for same_word in flatlist:
                if word==same_word:
                    freq +=1
            words[word]= freq
                
        for key,value in words.items():
            outstring=""
            outstring+=key +":" + str(value)
            outstring+="\n"
            outstream.write(outstring)
                    
        
            
        
            
            
                


















    
    
