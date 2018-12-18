strings = "{'hasError': False, 'errorId': '', 'errorDesc': '', 'data': {'cmpResultList': [{'cmpVecId': 'ab59051d-53a4-4666-b4d9-1c24e5a368ab', 'score': 3.757677413714646}], 'thresholdScore': -7}}"
print(strings)
speakin_result = eval(strings)
cmpResultList = speakin_result['data']['cmpResultList'][0]
thresholdScore = speakin_result['data']['thresholdScore']
print(thresholdScore)


score = a['score']
print(score)
