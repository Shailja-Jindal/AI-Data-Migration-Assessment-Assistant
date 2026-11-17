import pandas as pd
import streamlit as st

from migration_agent import assess_migration

st.title("AI Data Migration Assistant")

uploaded_file = st.file_uploader(
    "Upload Oracle Schema CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Schema Preview")

    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tables",
            df["table_name"].nunique()
        )

    with col2:
        st.metric(
            "Columns",
            len(df)
        )

    if st.button("Analyze Migration"):

        result = assess_migration(
            df.to_string()
        )

        st.markdown(result)

        st.download_button(
            label="Download Assessment",
            data=result,
            file_name="migration_assessment.md",
            mime="text/markdown"
        )