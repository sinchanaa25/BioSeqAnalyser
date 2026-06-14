import streamlit as st
from Bio.Seq import Seq
import pandas as pd

st.title("BioSeq Analyzer")

sequence = st.text_area("Enter DNA Sequence")

if st.button("Analyze"):

    sequence = sequence.upper().strip()

    if len(sequence) == 0:
        st.error("Please enter a DNA sequence.")
        st.stop()

    valid = set("ATGC")

    if not set(sequence).issubset(valid):
        st.error("Only A, T, G, and C are allowed.")
        st.stop()

    seq = Seq(sequence)

    length = len(sequence)

    gc = ((sequence.count("G") +
           sequence.count("C")) / length) * 100

    reverse_complement = seq.reverse_complement()

    st.subheader("Results")

    st.write("Length:", length)
    st.write("GC Content:", round(gc, 2), "%")
    st.write("Reverse Complement:", str(reverse_complement))

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    df = pd.DataFrame(
        counts.items(),
        columns=["Nucleotide", "Count"]
    )

    st.table(df)

    chart_df = df.set_index("Nucleotide")

    st.bar_chart(chart_df)