# WF-PPG Dataset

## Overview

Welcome to the WF-PPG dataset repository! This dataset, "WF-PPG: A Wrist-Finger Dual-channel Dataset," is designed to study the impact of wrist postures on Photoplethysmography (PPG) morphology. It is intended to facilitate research into how varying contact pressures between PPG sensors and the skin affect the quality of the PPG signals, particularly for wearable health monitoring applications.

## Contents

- [Introduction](#introduction)
- [Dataset Description](#dataset-description)
- [Data Structure](#data-structure)
- [File Fields and Descriptions](#file-fields-and-descriptions)
- [Contact](#contact)
- [Suggested Usage](#suggested-usage)
- [Contact](#contact)

## Introduction

Photoplethysmography (PPG) is a non-invasive optical technique commonly used in wearable devices for continuous health monitoring. However, the accuracy and reliability of PPG-based metrics such as heart rate and blood pressure can be compromised by variations in contact pressure between the PPG sensor and the skin. This dataset was created to provide a comprehensive resource for analyzing the effects of contact pressure on PPG signal morphology.

The dataset includes synchronized PPG signals from the wrist and fingertip, recorded under varying contact pressures using a custom-built device. Additional data such as ECG, blood pressure, and oxygen saturation are also included to provide a holistic view of each measurement session.

## Dataset Description

The WF-PPG dataset comprises synchronised data collected from 27 participants. For each participant, data was recorded under different contact pressure conditions across multiple sessions. The dataset includes:

- **Wrist PPG Signals**: PPG signals recorded from a sensor on the right wrist with varying contact pressure.
- **Finger PPG Signals**: Ideal PPG signals from a sensor on the right index fingertip under optimal contact pressure.
- **ECG Signals**: ECG signals from a chest band reflecting exact heartbeat timings.
- **Contact Pressure**: Readings from a load cell measuring the contact pressure between the wrist PPG sensor and the skin.
- **Blood Pressure**: Systolic and diastolic blood pressure measurements taken at the beginning of each session.
- **Oxygen Saturation**: Blood oxygen levels recorded from a pulse oximeter on the base of the right ring finger.

## Data Structure

Each subject directory includes files for the six recording sessions the subject underwent. Specifically, each session is documented with two files: 

1) A metrics and signals file labeled as *[Session Number]\_preprocessed\_[subjectID].csv*, which contains information such as synchronized PPG and ECG signals and blood pressure readings; 

2) A waveform indices and classes file labeled as *[Session Number]\_indices\_[subjectID].csv*, which contains the start and end points of each valid waveform in the recorded PPG signals and their morphology type based on the proposed classification scheme. 

In addition to these session-specific files, there is a global file named *additional\_info.csv* located in the root directory of the dataset, containing demographic information such as age, height, and weight for each subject.

The dataset file structure is as follows:

```
WF-PPG-Dataset/
│
├── <Participant ID>/
│ ├── <Session ID>/
│ │ ├── <Session ID>_preprocessed_<Participant ID>.csv
│ │ ├── <Session ID>_indices_<Participant ID>.csv
│ ├── <Session ID>/
│ └── ...
│
├── <Participant ID>/
│ └── ...
│
└── README.md
└── additional_info.csv
```

## File Fields and Descriptions

### `#_preprocessed_###.csv`

| Field               | Description                                                                          |
|---------------------|--------------------------------------------------------------------------------------|
| `Time`              | Timestamp in seconds from the beginning of the experiment                            |
| `PPG_Wrist_G`       | Raw PPG signals collected from the wrist clamp device (Green)                        |
| `PPG_Wrist_IR`      | Raw PPG signals collected from the wrist clamp device (Infrared)                     |
| `PPG_Wrist_R`       | Raw PPG signals collected from the wrist clamp device (Red)                          |
| `PPG_Finger_G`      | Raw PPG signals collected from the PPG sensor strapped to the fingertip (Green)      |
| `PPG_Finger_IR`     | Raw PPG signals collected from the PPG sensor strapped to the fingertip (Infrared)   |
| `PPG_Finger_R`      | Raw PPG signals collected from the PPG sensor strapped to the fingertip (Red)        |
| `Pressure_In`       | Reading from the load cell which measures pressure between the wrist PPG sensor and the wrist |
| `ECG`               | ECG signal from the ECG chest band                                                   |
| `BP_Sys`            | Systolic blood pressure measurement                                                  |
| `BP_Dia`            | Diastolic blood pressure measurement                                                 |
| `SpO2`              | Oxygen saturation measured with a pulse oximeter                                     |
| `PPG_Wrist_G_AC`    | Preprocessed wrist PPG signal measured with green light                              |
| `PPG_Finger_G_AC`   | Preprocessed finger PPG signal measured with green light                             |
| `PPG_Finger_IR_AC`  | Preprocessed finger PPG signal measured with infrared light                          |
| `PPG_Finger_R_AC`   | Preprocessed finger PPG signal measured with red light                               |

### `#_indices_###.csv`

| Field      | Description                                          |
|------------|------------------------------------------------------|
| `finger_s` | Starting index of waveform from the finger           |
| `finger_e` | Ending index of waveform from the finger             |
| `finger_t` | Class of waveform from the finger                    |
| `wrist_s`  | Starting index of waveform from the wrist            |
| `wrist_e`  | Ending index of waveform from the wrist              |
| `wrist_t`  | Class of waveform from the wrist                     |

## Suggested Usage
The WF-PPG dataset is ideal for observing variations in PPG waveforms recorded from the wrist compared to the fingertip, especially under different contact pressures. Users can analyze these variations using the PPG_Wrist_G, PPG_Wrist_IR, and PPG_Wrist_R fields alongside the Pressure_In data to understand the impact of contact pressure on signal quality. The synchronized ECG signals (ECG field) provide ground truth heartbeat timings, essential for validating heart rate and other cardiovascular metrics derived from PPG signals. Additionally, metrics like blood pressure (BP_Sys, BP_Dia) and oxygen saturation (SpO2) can be used to evaluate and improve signal processing methods, enhancing the accuracy and reliability of wearable health monitoring systems.

### Potential Dataset Uses
Here are some potential research applications:

**Signal Quality Assessment:** Investigate how contact pressure variations affect PPG signal morphology.

**PPG Signal Enhancement Methods:** Develop algorithms to compensate for signal distortions caused by contact pressure.

**Continuous Health Monitoring:** Analyze the feasibility of wrist-based PPG for reliable health metrics extraction.

## Contact
For any questions or suggestions, please reach out to:

Matthew Ho matthewho.2021@scis.smu.edu.sg