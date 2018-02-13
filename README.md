Approach-
1. Store the records in a dictionary(fullrecords)
2. Store the records which have unique name and zipcode(name_zip_revrecords)
3. As soon as a record with a non-unique name and zipcode is encountered, store the record in a different dictionary with unique cmtd id, zipcode and year fields(cmteid_zip_year_records)
4. Append donation values to the above dictonary of the records of a repeat donor
5. Calculate the percentile on every unique list of values of (cmtdid, zipcode and year)
6. Output the finalized rpeat donor records

Dependancies-
Please import the following library-
import math 