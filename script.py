mport os
import collections
import socket

#List all files in the directory
files = os.listdir('/home/data')
print("Text files in the directory:", files)

total_words = 0
word_counts = {}
for file in files:
    if file.endswith('.txt'):
        with open(f'/home/data/{file}', 'r') as f:
            words = f.read().split()
            word_count = len(words)
            print(f'Number of words in {file}: {word_count}')
            total_words += word_count

            # Count words for the specific file 'IF.txt'
            if file == 'IF.txt':
                for word in words:
                    if word not in word_counts:
                        word_counts[word] = 0
                    word_counts[word] += 1

print("Total number of words in all files:", total_words)

#List the top 3 words in 'IF.txt'
if 'IF.txt' in files:
    top_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:3]
    print("Top 3 words in IF.txt:", top_words)

#Find and print the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())
print("IP address of the machine:", ip_address)

#Write all the output to a result file
with open('/home/output/result.txt', 'w') as f:
    f.write("List of text files: " + ', '.join(files) + "\n")
    f.write("Total number of words in all files: " + str(total_words) + "\n")
    f.write("Top 3 words in IF.txt: " + str(top_words) + "\n")
    f.write("IP address of the machine: " + ip_address + "\n")

#Print the contents of the result file
with open('/home/output/result.txt', 'r') as f:
    print(f.read())
