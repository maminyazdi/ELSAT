# Event Log Synchronization and Abstraction Tool (ELSAT)

## Description

ELSAT is a Python program designed to synchronize two event logs and abstract them based on the similarity of events. This tool aids in the transformation of fine-granular event logs from client-server applications to a higher level of abstraction, making it easier for domain experts to analyze. The foundation of this program is rooted in a comprehensive research paper, which provides an overview of existing literature and introduces a novel approach to event log abstraction.

## Features

- **Log Synchronization**: Efficiently synchronizes two distinct event logs.
- **Event Abstraction**: Processes raw event logs to generate an abstracted, human-readable format based on event similarities.
- **Intuitive Analysis**: Generates abstracted models which are geared towards domain experts for a more straightforward process analysis.
- **Research-backed**: Based on the latest advancements in process mining techniques as discussed in the accompanying research paper.

## Requirements

- Python 3.7+
- Necessary Python libraries (see `requirements.txt`)

## Installation

1. Clone the repository:
\```bash
git clone https://github.com/user/elsat.git
\```

2. Navigate to the cloned directory:
\```bash
cd elsat
\```

3. Install required Python packages:
\```bash
pip install -r requirements.txt
\```

## Usage

1. Make sure both event logs are in the correct format (e.g., CSV, JSON).
2. Run the ELSAT tool:
\```bash
python main.py --log1 <path_to_log1> --log2 <path_to_log2> --output <path_to_output>
\```

## Parameters

- `--log1`: Path to the first event log file.
- `--log2`: Path to the second event log file.
- `--output`: Path where the synchronized and abstracted log should be saved.


## Contribution

Feel free to fork the repository and submit pull requests for improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## Citation

If you are using ELSAT in your research or toolchain, please cite our accompanying research paper: `DOI: 10.5220/0010652000003064`

