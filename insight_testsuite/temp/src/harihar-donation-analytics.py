
# coding: utf-8

# In[2]:


import math
import datetime
f = open("input\itcont.txt",'r')
inputFile = f.readlines()                                   #read the inputfile line by line and store it
f = open("input\percentile.txt",'r')
percentile_to_find = f.read()                               #read the percentile value and store it


# In[3]:


fullrecords={}
count=0
for line in inputFile:                                      #store each line in the dictionary
    temp=line
    fullrecords[count]=line
    count=count+1   
print(fullrecords)    


# In[4]:


name_zip_revrecords={}                                      #dictionary to store the record by unique (name, zipcode)
cmteid_zip_year_records={}                                  #dictionary to store the record by unique (cmteid, zipcode, year) 

for rec in fullrecords.values():
    temp=rec.split("|")
    if(not temp[15] and temp[0] and temp[14] and temp[10] and len(temp[10])>4 and temp[13] and temp[7]):
        if((temp[7], temp[10][:5])) in name_zip_revrecords:                                                 #record already present in (name, zip) hence repeat donor
            if((temp[0], temp[10][:5], temp[13][-4:])) in cmteid_zip_year_records:                          #calculating repeat donors so far for that calendar year, recipient and zip code
                cmteid_zip_year_records[(temp[0], temp[10][:5], temp[13][-4:])].append(int(temp[14]))       #record already present (cmteid, zipcode, year), append the transaction amount
            else:
                cmteid_zip_year_records[(temp[0], temp[10][:5], temp[13][-4:])]=[int(temp[14])]             #store unique record (cmteid, zipcode, year)       
        name_zip_revrecords[(temp[7], temp[10][:5])]=[temp[0], temp[13][-4:], temp[14], temp[15]]               #store unique record(name, zipcode)
print(cmteid_zip_year_records)        


# In[6]:


with open("output/repeat_donors.txt",'w') as f:
    for cmteid, zipcode, year in cmteid_zip_year_records:
        individual_donations=[]                                                   #list of donations for a particular recepient
        individual_donations=cmteid_zip_year_records[cmteid, zipcode, year]       
        individual_donations.sort()                                               #sorting the donations in ascending order for calculating percentile value
        length=len(individual_donations)                                          
        percentile_index = math.ceil(int(percentile_to_find)*length/100)-1        #calculating the percentile index based on formula for nearest-rank method
        percentile_value = individual_donations[percentile_index]
        total_contribution=0                                                      
        index=0
        for x in cmteid_zip_year_records.get((cmteid, zipcode, year)):
            total_contribution+=x                                                 #The cumilative contribution for a record
            index+=1
            repeat_donors_record= cmteid + "|" + zipcode + "|" + year + "|" + str(percentile_value) + "|" + str(total_contribution) + "|" + str(index) + "\n" 
            f.write(repeat_donors_record)                                         #output the record to file

