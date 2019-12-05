import os
import numpy
from collections import defaultdict
import operator
import csv

file = open('03-Python_Python-HW_Instructions_PyPoll_Resources_election_data.csv', "rU")
reader = csv.reader(file, delimiter=',')

candidate_dict = defaultdict(int)
ratio_dict = defaultdict(float)
vote_total = 0
count = 0

for column in reader:
    if count >= 1:
        #grab the candidate out of the row
        cand = column[2]
        vote_total = vote_total + 1
        #increment the spot in our dictionary that corresponds to the candidate
        candidate_dict[cand]+=1
        #percentage of votes that each candidate received
        ratio_dict[cand] = candidate_dict[cand] / vote_total
    count+=1
    

print('!!!!!!!!!!!!!!!!!!!!!!!!!!')   

print('total votes : ' + str(vote_total))
print('List of candidates receiving votes: ' + str(list(candidate_dict.keys())))
print('Vote percentages: ' + str(list(ratio_dict.items())))
print('Vote Totals : ' + str(list(candidate_dict.items())))

#Sort our dictionary to get the candidate with the most votes. 
sorted_d = sorted(candidate_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)
print('Winner : ' + str(sorted_d[0]))





text_file = open("election_output.txt", "w")
text_file.write('total votes : ' + str(vote_total))
text_file.write('\n')
text_file.write('List of candidates receiving votes: ' + str(list(candidate_dict.keys())))
text_file.write('\n')
text_file.write('Vote percentages: ' + str(list(ratio_dict.items())))
text_file.write('\n')
text_file.write('Vote Totals : ' + str(list(candidate_dict.items())))
text_file.write('\n')
text_file.write('Winner : ' + str(sorted_d[0]))
text_file.close()
