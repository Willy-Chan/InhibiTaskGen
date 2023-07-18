# Inhibition-Control Task Trial Generator

This Python script generates a CSV file with randomly generated data representing stimuli for an inhibition control decision task. It creates a dataset with four columns: `red_shape`, `green_shape`, `white_shape`, and `match`. In the proposed model, the red shape serves as a distractor, while the target (green) and probe (white) shapes are compared to one another by a user.

## Overview

The script generates random values for `red_shape`, `green_shape`, and `white_shape` columns, ranging from 1 to 10 inclusive. The `match` column indicates whether the `green_shape` and `white_shape` values match. If they match, the `match` value is set to 1; otherwise, it is set to 0.

## Inspiration

This script was inspired by the research paper titled "[The Influence of Cognitive Control on Performance and Learning in ADHD: A Review](https://scienceofbehaviorchange.org/wp-content/uploads/2017/07/FriedmanMiyake2004-1.pdf)" by Friedman and Miyake (2004). The paper explores the relationship between cognitive control processes and attention deficit hyperactivity disorder (ADHD).

## ROAR-Shape

This data generator serves as a supplement to ROAR-Shape, an open-source reading assessment tool being developed by the Yeatman lab. ROAR-Shape aims to diagnose ADHD and dyslexia in children. The generated data can be used for testing and evaluation purposes within the context of ROAR-Shape.

For more information about ROAR-Shape and the Yeatman lab, please refer to their official resources.

## Requirements

- Python (version 3.x)
- `csv` module (included in Python's standard library)

## Usage

1. Clone this repository or download the `coin_flip_data_generator.py` script.
2. Ensure you have Python installed on your system.
3. Install the required `csv` module if not already available.
4. Run the script using the command: `python coin_flip_data_generator.py`
5. The generated CSV file named "coin_flip_data.csv" will be created in the same directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Yeatman lab for their work on ROAR-Shape.
- Friedman, N.P., & Miyake, A. (2004). The influence of cognitive control on performance and learning in ADHD: A review. _Clinical psychology review, 24_(7), 833-857.
