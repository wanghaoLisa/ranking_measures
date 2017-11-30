# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 11:25:49 2017

@author: haow5
"""

import measures



file_name = 'Copy of NetworkDistance-supermarket0622 - 0626remove149-rankDCG0710.xlsx'
import pandas as pd
xl_workbook = pd.ExcelFile(file_name)  # Load the excel workbook
df = xl_workbook.parse("Sheet1paper")  # Parse the sheet into a dataframe
#==============================================================================
# MapRankList = df['MapRank'].tolist()  # Cast the desired column into a python list
#==============================================================================

                
#RankMedianAvgList = df['RankMedianAvg'].tolist()  # Cast the desired column into a python list

#RankInverseSumList = df['RankInverseSum'].tolist()  # Cast the desired column into a python list

RanknormalizedScoreEqList = df['RanknormalizedScoreEq'].tolist()  # Cast the desired column into a python list
#GoldFirstRankingList = df['GoldFirstRanking'].tolist()  # Cast the desired column into a python list
#MapRankList = df['MapRank'].tolist()  # Cast the desired column into a python list                

                
L1=RanknormalizedScoreEqList
RankNetworkDistanceAvgList = df['RankNetworkDistanceAvg'].tolist()  # Cast the desired column into a python list
RankNetworkDistanceEqList = df['RankNetworkDistanceEq'].tolist()
                               
RankEuclideanDistanceAvgList = df['RankEuclideanDistanceAvg'].tolist()  # Cast the desired column into a python list
RankEuclideanDistanceEqList = df['RankEuclideanDistanceEq'].tolist()                            
                                 
                                 
RankManhattanDistanceAvgList = df['RankManhattanDistanceAvg'].tolist()  # Cast the desired column into a python list
RankManhattanDistanceEqList = df['RankManhattanDistanceEq'].tolist()
                                 
RankIntersectionAvgList = df['RankIntersectionAvg'].tolist()  # Cast the desired column into a python list
RankIntersectionEqList = df['RankIntersectionEq'].tolist()
                            
RankTurnAvgList = df['RankTurnAvg'].tolist()  # Cast the desired column into a python list
RankTurnEqList = df['RankTurnEq'].tolist()
                    
RankAngleAvgList = df['RankAngleAvg'].tolist()  # Cast the desired column into a python list
RankAngleEqList = df['RankAngleEq'].tolist()
                     
RankTDAvgList = df['RankTDAvg'].tolist()  # Cast the desired column into a python list
RankTDEqList = df['RankTDEq'].tolist()


def test_measures(reference, hypothesis):
    """
    Runs all rank-ordering evaluation measures on given pair of lists.
    """

    print "\t DCG:\t\t\t", measures.find_dcg(hypothesis)
    print "\t nDCG:\t\t\t", measures.find_ndcg(reference, hypothesis)
    print "\t Precision:\t\t", measures.find_precision(reference, hypothesis)
    print "\t Precision at k:\t", measures.find_precision_k(reference, hypothesis, len(reference))
    print "\t Average precision:\t", measures.find_average_precision(reference, hypothesis)
    print "\t RankDCG:\t\t", measures.find_rankdcg(reference, hypothesis), "\n"

#Defining test cases
#L1 = [9, 4, 4, 2, 2, 2, 0, 0, 0, 0]
#L2 = [9, 4, 4, 2, 2, 0, 2, 0, 0, 0]
#L3 = [4, 4, 2, 9, 2, 2, 0, 0, 0, 0]
#L4 = [0, 4, 4, 2, 2, 2, 9, 0, 0, 0]
#L5 = [0, 4, 4, 2, 2, 2, 0, 0, 0, 9]
#L6 = [0, 0, 0, 0, 2, 2, 2, 4, 4, 9]

#Testing:
print "1. RankNetworkDistanceAvgList"
test_measures(L1, RankNetworkDistanceAvgList)

print "1.1 RankNetworkDistanceEqList"
test_measures(L1, RankNetworkDistanceEqList)

print "2. RankEuclideanDistanceAvgList"
test_measures(L1, RankEuclideanDistanceAvgList)

print "2.1 RankEuclideanDistanceEqList"
test_measures(L1, RankEuclideanDistanceEqList)

print "3. RankManhattanDistanceAvgList"
test_measures(L1, RankManhattanDistanceAvgList)

print "3.1 RankManhattanDistanceEqList"
test_measures(L1, RankManhattanDistanceEqList)

print "4. RankIntersectionAvgList"
test_measures(L1, RankIntersectionAvgList)

print "4.1 RankIntersectionEqList"
test_measures(L1, RankIntersectionEqList)

print "5. Case RankTurnAvgList"
test_measures(L1, RankTurnAvgList)

print "5.1 Case RankTurnEqList"
test_measures(L1, RankTurnEqList)

print "6. The RankAngleAvgList case (reverse ordering):"
test_measures(L1, RankAngleAvgList)

print "6.1 The RankAngleEqList case (reverse ordering):"
test_measures(L1, RankAngleEqList)

print "7. The RankTDAvgList case (reverse ordering):"
test_measures(L1, RankTDAvgList)

print "7.1 The RankTDEqList case (reverse ordering):"
test_measures(L1, RankTDEqList)

print "L1"
print L1