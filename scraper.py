import requests
from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, filing_year):
    # Sample URL structure - change it based on court portal
    url = f"https://services.ecourts.gov.in/ecourtindia_v6/?case_type={case_type}&case_number={case_number}&case_year={filing_year}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if "captcha" in response.text.lower():
        raise Exception("CAPTCHA encountered")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Parse fields
    parties = soup.find_all("div", class_="party-name")
    hearing_dates = soup.find_all("div", class_="hearing-date")
    pdf_links = soup.find_all("a", href=lambda href: href and "pdf" in href)

    return {
        "parties": [p.text.strip() for p in parties],
        "hearings": [h.text.strip() for h in hearing_dates],
        "pdfs": [l['href'] for l in pdf_links]
    }
