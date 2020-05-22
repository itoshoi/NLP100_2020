sort -n -k 3 -r ../popular-names.txt > output_py.txt
python NPL100_18.py ../popular-names.txt > output_unix.txt
diff output_py.txt output_unix.txt