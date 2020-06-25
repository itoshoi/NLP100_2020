curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=0B7XkCwpI5KDYNlNUTTlSS21pQmM" -o "GoogleNews-vectors-negative300.bin.gz"