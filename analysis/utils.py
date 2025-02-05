import requests 
from bs4 import BeautifulSoup
from datetime import datetime

from analysis.models import DigitalStatistics


def get_lottery_data():
    # Define the URL
    current_year = datetime.now().year
    # Set headers to mimic a real browser request (optional but recommended)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for year in range(2004, current_year + 1):
        url = f"https://www.cpzhan.com/lotto649/all-results.php?year={year}"
        # Send a GET requst to the website
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the <div class="mytable">
            div_table = soup.find("div", class_="mytable")

            if div_table:
                # Find the <table> inside <div class="mytable">
                table = div_table.find("table")

                if table:
                    # Find the <tbody> inside <table>
                    tbody = table.find("tbody")

                    if tbody:
                        # Find all <tr> inside <tbody>
                        rows = tbody.find_all("tr")

                        # Extract <td> content from each <tr>
                        for row in rows:
                            columns = row.find_all("td")
                            row_data = [col.text.strip() for col in columns]
                            
                            if row_data:
                                result = {
                                    "year": row_data[0],
                                    "draw_number": row_data[1],
                                    "draw_date": row_data[2],
                                    "numbers": row_data[3:]
                                }
                                record_lotto_numbers(result)
                                
                    else:
                        print("No <tbody> found inside <table>.")
                else:
                    print("No <table> found inside <div class='mytable'>.")
            else:
                print("No <div class='mytable'> found.")
        else:
            print("Failed to retrieve the page:", response.status_code)


def record_lotto_numbers(result):
    """
    Records the frequency of each lottery number appearing in the results.
    
    Args:
    result: A dictionarie, each representing a lotto result.
    """
    numbers = result["numbers"]
    for number in numbers:
        stat, created = DigitalStatistics.objects.get_or_create(
            number=number,
            defaults={'times': 0}
        )
        # Increment the 'times' field by 1 for this number
        stat.times += 1
        stat.save()