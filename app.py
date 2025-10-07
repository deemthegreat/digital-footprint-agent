# app.py (The Streamlit User Interface)
import streamlit as st
from crew import run_footprint_analysis # Import your crew function

st.set_page_config(layout="centered")

st.title("🤖 The Zero-Cost Cluster & Score Bot")
st.markdown("Your unique AI agent for deep digital footprint analysis and risk scoring.")

# User Input
target_name = st.text_input(
    "Enter the Name/Username/Email to Scan:",
    placeholder="e.g., JaneDoe1985, janedoe@company.com"
)

if st.button("Start Reconnaissance", type="primary"):
    if not target_name:
        st.warning("Please enter a name or identifier to start the scan.")
    else:
        # Use st.status to show the progress in real-time
        with st.status("Running AI Reconnaissance and Risk Analysis...", expanded=True) as status:
            st.write(f"Starting scan for: **{target_name}**")
            
            # The AI Agent runs here!
            final_report = run_footprint_analysis(target_name)
            
            # Once done, update the status and display the report
            status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
        
        st.success("Analysis complete! See the unique report below.")
        st.markdown(final_report)
        
        # This is where you can insert your FEE/REVENUE pitch (optional for the free app)
        st.info("💡 **Like the unique risk score?** The Pro Version offers automated cleanup and dark web scanning for a small fee.")