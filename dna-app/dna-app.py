import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

#########################
# Page Title
#########################

# Open the image of the project
image = Image.open("dna-logo.jpg")

# print the image in the web App
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App
         
This app counts the nucleotide composition of query DNA!
""")
         
#########################
# text Area
#########################

st.header("Enter the DNA sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("sequence input", sequence_input, height=150)
sequence =sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
***
""")

## print the input DNA
st.header("INPUT (DNA QUERY)")
sequence

## DNA nucleotide count
st.header("OUTPUT (DNA QUERY COUNTS)")

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

# print the nucleotide on the web App
X

st.subheader("2. Print Text")
st.write("There are " + str(X['A']) + " adenine (A)")
st.write("There are " + str(X['T']) + " thymine (T)")
st.write("There are " + str(X['G']) + " Guanine (G)")
st.write("There are " + str(X['A']) + " cytosine (C)")

# Dispaly Dataframe
st.subheader("3. Display Dataframe")
df =pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: "count"}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {"index": "nucleotides"})
st.write(df)

# Display a bar chart
st.subheader("4. display Bar Chart using Altair")
p = alt.Chart(df).mark_bar().encode(
    x='nucleotides',
    y= 'count'
)
p = p.properties(
    width=alt.Step(80),    
)

st.write(p)