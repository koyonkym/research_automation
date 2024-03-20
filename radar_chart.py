from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from datetime import datetime


class RadarChart:
    def __init__(self, base: str, segments: list[str]):
        self.base = base
        self.segments = segments

    def get_search_results_count(self, query: str) -> int:
        # Launch Chrome browser
        driver = webdriver.Chrome()

        self.search(driver, query)

        # Find the search result stats element
        try:
            result_stats = driver.find_element(By.ID, "result-stats").text
        except:
            self.search(driver, query)

        # Extract the number of search results
        if result_stats == "":
            count = 0
        else:
            count = self.extract_number(result_stats)

        # Close the browser
        driver.quit()

        return count

    def search(self, driver: webdriver.chrome.webdriver.WebDriver, query: str):
        # Open Google search
        driver.get("https://www.google.com/")

        # Find the search box element
        search_box = driver.find_element(By.NAME, "q")

        # Input the search query
        search_box.send_keys(query)

        # Submit the search query
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(2)

    def extract_number(self, text: str) -> int:
        # Define a regular expression pattern to match numbers
        pattern = r'\d{1,3}(?:,\d{3})*'

        # Find all matches of the pattern in the text
        matches = re.findall(pattern, text)

        number = matches[0]

        # Convert the string number to an integer
        number = int(number.replace(',', ''))

        return number

    def create_rader_chart(self, labels: list[str], values: list[int]):
        # Number of variables
        num_vars = len(labels)

        # Compute angle for each axis
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # Complete the loop
        values=np.concatenate((values,[values[0]]))
        angles=np.concatenate((angles,[angles[0]]))

        # Plot
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values, color='skyblue', alpha=0.6)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=12)

        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Save the figure with current date and time
        plt.savefig(f'radar_chart_{current_datetime}.png', dpi=300)  # Save as PNG format with 300 dpi resolution

    def create(self):
        queries = self.segments
        result_counts = []
        for query in queries:
            result_count = self.get_search_results_count(self.base + " " + query)
            if result_count == 0:
                result_count = self.get_search_results_count(self.base + " " + query)
                result_counts.append(result_count)
            else:
                result_counts.append(result_count)
        self.result_counts = result_counts
        self.create_rader_chart(queries, result_counts)

if __name__ == "__main__":
    # base = "生成AI"
    base = "Generative AI"
    # segments = ["製造", "医療", "金融", "教育", "小売", "不動産", "エネルギー", "飲食", "観光", "エンターテイメント", "農業", "建設"]
    segments = ["Manufacturing", "Medical", "Finance", "Education", "Retail", "Property", "Energy", "Food", "Tourism", "Entertainment", "Agriculture", "Construction"]
    radar_chart = RadarChart(base=base, segments=segments)
    radar_chart.create()