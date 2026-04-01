import streamlit as st
from crypto_utils import encode_message, decode_message, save_to_file, load_from_file

st.set_page_config(page_title="Secure Message App", page_icon="🔐")

st.title("🔐 Secure Message Encoder & Decoder")

# Inputs
message = st.text_area("Enter Message")
key = st.text_input("Enter Secret Key", type="password")

# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Encode"):
        if message and key:
            result = encode_message(message, key)
            st.success("Encrypted Message:")
            st.code(result)
            st.session_state.result = result
        else:
            st.error("Enter message and key")

with col2:
    if st.button("Decode"):
        if message and key:
            result = decode_message(message, key)
            st.success("Decrypted Message:")
            st.code(result)
        else:
            st.error("Enter message and key")

# Save & Load
st.subheader("💾 Save / Load")

if st.button("Save Encrypted Message"):
    if "result" in st.session_state:
        save_to_file(st.session_state.result)
        st.success("Saved to file")
    else:
        st.error("No encrypted message to save")

if st.button("Load Encrypted Message"):
    data = load_from_file()
    st.text_area("Loaded Message", value=data, height=100)

# Copy info
st.info("Copy text manually from above box")