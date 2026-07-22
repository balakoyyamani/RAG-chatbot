from pprint import pprint

def chunk_text(text,chunk_size=5):
    chunks=[]
    for i in range(0,len(text),chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def chunk_by_word(text,chunk_size=5):
    words=text.split()
    chunks=[]
    for i in range(0,len(words),chunk_size):
        chunks.append(words[i:i+chunk_size])
    return chunks

def chunk_with_overlap(text,chunk_size=5,overlap=2):
    words=text.split()
    chunks=[]
    start=0
    while(start<len(words)):
        end=start+chunk_size
        chunks.append(" ".join(words[start:end]))
        start=end-overlap
    pprint(chunks)

chunk_with_overlap("Hello I am Bala and I done my engineering in Panimalar Engineering College")