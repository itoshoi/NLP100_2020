python NPL100_19.py ../hightemp.txt | tee output_py.txt
cut -f 1 ../hightemp.txt | sort | uniq -c | sort -r | tee output_unix.txt
# diff output_py.txt output_unix.txt