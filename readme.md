# Research Automation Project

This project automates the process of querying Google using Selenium, extracting the search result counts, and visualizing them with a radar chart.

## Description

The project utilizes:

- Python
- Selenium
- Matplotlib (with Japanize-Matplotlib for Japanese labels)
- Regular expressions
- Chrome WebDriver

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/koyonkym/research_automation.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Modify the `base` and `segments` list in the script with your desired search terms.
2. Run the script:

    ```bash
    python radar_chart.py
    ```

3. The script will perform Google searches, extract the result counts, and generate a radar chart.

## Example

```python
python radar_chart.py
```

## License

This project is licensed under the [MIT License](LICENSE).