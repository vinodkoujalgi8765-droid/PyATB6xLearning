test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

result = filter(lambda x:x=="PASS", test_results)
print(tuple(result))

result1 = map(lambda x:x=="FAIL", test_results)
print(list(result1))