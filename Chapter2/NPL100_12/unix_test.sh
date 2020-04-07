cut -f 1 ../hightemp.txt > col1_unix.txt
cut -f 2 ../hightemp.txt > col2_unix.txt
diff -s col1.txt col1_unix.txt
diff -s col2.txt col2_unix.txt