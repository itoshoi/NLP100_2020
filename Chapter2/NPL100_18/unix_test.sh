sort -k 3 -r ../hightemp.txt > output_py.txt
python NPL100_18.py ../hightemp.txt > output_unix.txt
diff output_py.txt output_unix.txt