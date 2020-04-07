python NPL100_17.py ../hightemp.txt | sort > output_python.txt
cut -f 1 ../hightemp.txt | sort | uniq > output_unix.txt
diff -s output_python.txt output_unix.txt