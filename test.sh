cd LocalTests
# clear out the circle and person txt files
rm outputs/circle_test_output.txt
rm outputs/person_test_output.txt
bash run_person.sh
bash run_circle.sh