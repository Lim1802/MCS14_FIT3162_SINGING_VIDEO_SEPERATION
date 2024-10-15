import streamlit as st
import subprocess
import os
from streamlit_js_eval import streamlit_js_eval



st.title("Music Separation 🎶")

# Initialize session state variables
if 'seperated_audio' not in st.session_state:
    st.session_state.seperated_audio = ''

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = ''

def del_files():
    streamlit_js_eval(js_expressions="parent.window.location.reload()")



# File uploader
st.session_state.uploaded_file = st.file_uploader("Choose a WAV or MP3 file", type=["wav", "mp3"])

if st.session_state.uploaded_file:
    uploaded_file = st.session_state.uploaded_file

    # Log file upload status
    print(f"File {uploaded_file.name} uploaded successfully.")

    # Display the uploaded audio file
    if uploaded_file.type == "audio/mp3":
        st.audio(uploaded_file, format="audio/mp3")
        with open("temp_input.mp3", "wb") as f:
            f.write(uploaded_file.getvalue())
        print("MP3 file saved as temp_input.mp3.")
    else:
        st.audio(uploaded_file, format="audio/wav")
        with open("temp_input.wav", "wb") as f:
            f.write(uploaded_file.getvalue())
        print("WAV file saved as temp_input.wav.")

    # Button to start processing
    if st.button("Separate Audio Sources"):
        print("Separation process started...")
        with st.spinner('Processing audio...'):

            print(f"{uploaded_file.name} is being passed to the separation model...")
            # Update the command to include the output directory
            command = f"python -m demucs.separate -o output temp_input.wav"
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

        if process.returncode == 0:
            st.success("Audio separation completed successfully!")
            print("Audio separation successful.")
            output_dir = "output/htdemucs/temp_input"
            st.session_state.seperated_audio = output_dir

            # Print list of separated files
            if os.path.exists(output_dir):
                print(f"Separation output stored in: {output_dir}")
                for file in os.listdir(output_dir):
                    if file.endswith(".wav"):
                        print(f"Separated file: {file}")
        else:
            st.error("Error during audio separation. Please check your input file and try again.")
            print(f"Error occurred: {stderr.decode()}")

    # Display and download separated audio files
    if st.session_state.seperated_audio:
        output_dir = st.session_state.seperated_audio
        if os.path.exists(output_dir):
            for file in os.listdir(output_dir):
                if file.endswith(".wav"):
                    file_path = os.path.join(output_dir, file)
                    st.write(f"Separated {file}:")
                    st.audio(file_path, format="audio/wav")
                    with open(file_path, "rb") as f:
                        st.download_button(
                            label=f"Download {file}",
                            data=f,
                            file_name=file,
                            mime="audio/wav"
                        )
                    print(f"File {file} is ready for download.")

        restart = st.button("Restart", key="restart_button", on_click=del_files)
        if restart:
            print("Restart triggered, clearing files and session.")

    # Clean up temporary files
    if os.path.exists("temp_input.wav"):
        os.remove("temp_input.wav")
        print("Temporary input WAV file deleted.")