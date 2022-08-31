TC_CORRECT=0 # Test Case Correct Count
TC_INCORRECT=0 # Test Case Incorrect Count

# compare the output file with the expected output file
diff tests/outputs/person_test_out.txt tests/person_test_out_expected.txt
if [ $? -eq 0 ]; then
    #echo "Test Case 1: Correct"
    TC_CORRECT=$((TC_CORRECT+1))
else
    #echo "Test Case 1: Incorrect"
    TC_INCORRECT=$((TC_INCORRECT+1))
fi

# if TC_INCORRECT is 0, then all test cases were correct
if [ $TC_INCORRECT -eq 0 ]; then
    echo "All Test Cases Correct"
else
    echo "Simple Calculator did not pass all test cases"
fi
