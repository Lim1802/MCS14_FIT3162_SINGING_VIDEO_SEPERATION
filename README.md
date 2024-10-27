# MCS14 FIT3162 Final Year Project (Singing Video Generation with **Music Separation**)

## Project Overview

This project focuses on **developing a music decomposition system** that utilizes deep learning techniques to separate composite audio into distinct components, such as **vocals, bass, drums, and others**. The system is designed to enhance applications in music production, remixing, and audio analysis by providing high-quality audio separation.

## Features

- **Hybrid Model Architecture**: Utilizes a combination of time-domain and spectrogram-domain processing with Transformer layers for superior audio separation. Our model is has an overall SDR / NSDR of 4.54 / 4.93.
- **Web Application**: A user-friendly interface built with Streamlit allows users to upload audio files and download separated components using our own model.
- **Google Colab Integration**: Provides a comprehensive notebook for training and evaluating the model, facilitating easy replication and experimentation.

1. **Run the Streamlit Application**:
   - Download the "MCS14_Web_App.ipynb" file or open it directly in [Google Colab](https://colab.research.google.com/drive/1UTlQGmp50IhMLSsw3EFR_7rMIRpCJuMp?usp=sharing).
   - Execute the cells to start the Streamlit server and access the application via the provided URL.

2. **Training the Model**:
   - Download the "MCS14_Train_Evaluation.ipynb" file or open it directly in [Google Colab](https://colab.research.google.com/drive/1ExGalxkGIPy-M-c7e8co3bkUUsSP8CeD?usp=sharing).
   - Follow the instructions to set up the environment, upload datasets, and train the model.

## Requirements

### Hardware

- **For Music Separation**: Google Colab (Free Version) with at least 12 GB of RAM.
- **For Model Training**: Google Colab Pro+ with A100 GPU, 83.5 GB of RAM, and 235.7 GB of Disk Space.

## Usage

- **Uploading Files**: Users can upload audio files in WAV or MP3 formats through the web interface.
- **Processing Audio**: Click the "Separate Audio Sources" button to process the uploaded file.
- **Downloading Results**: Once processing is complete, download the separated audio components directly from the interface.

## Limitations

- **Complex Audio**: The model may struggle with very complex or overlapping audio sources.
- **Processing Time**: Larger or more complex files may require longer processing times.

## Future Work

- **Vocal Diarization**: Implement techniques to separate and identify individual vocal tracks.
- **Scalability**: Deploy the application on a cloud server to enhance accessibility and performance.


## Contact

For questions or support, please contact:
- Heng Zi Ying: zhen0009@student.monash.edu
- Lim Wei En: wlim0060@student.monash.edu
- Lim Jun Kee: jlim0211@student.monash.edu