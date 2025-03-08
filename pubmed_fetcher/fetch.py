import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

# ✅ Step 1: Fetch paper IDs from PubMed
def fetch_pubmed_papers(query: str, max_results: int = 10) -> List[str]:
    """Fetch PubMed paper IDs for a given search query."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return []

    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    return paper_ids

# ✅ Step 2: Fetch Paper Details
def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetch detailed information for a list of paper IDs from PubMed."""
    if not paper_ids:
        return []

    details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }

    response = requests.get(details_url, params=params)

    if response.status_code != 200:
        print(f"Error fetching paper details: {response.status_code}")
        return []

    # Parse XML response
    root = ET.fromstring(response.text)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        paper_data = {}

        # Extract Title
        title_elem = article.find(".//ArticleTitle")
        paper_data["Title"] = title_elem.text if title_elem is not None else "N/A"

        # Extract Pubmed ID
        pmid_elem = article.find(".//PMID")
        paper_data["PubmedID"] = pmid_elem.text if pmid_elem is not None else "N/A"

        # Extract Authors and Affiliations
        authors = []
        company_affiliations = []
        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            fore_name = author.find("ForeName")
            full_name = f"{fore_name.text} {last_name.text}" if last_name is not None and fore_name is not None else "N/A"
            
            affiliation_elem = author.find(".//Affiliation")
            affiliation = affiliation_elem.text if affiliation_elem is not None else "N/A"

            if affiliation != "N/A":
                authors.append(full_name)
                if any(word in affiliation.lower() for word in ["pharma", "biotech", "company", "inc.", "ltd.", "corporation"]):
                    company_affiliations.append(affiliation)

        paper_data["Authors"] = ", ".join(authors)
        paper_data["Company Affiliations"] = ", ".join(company_affiliations) if company_affiliations else "N/A"

        # Extract Corresponding Author Email
        email_elem = article.find(".//AffiliationInfo/Affiliation")
        paper_data["Corresponding Author Email"] = email_elem.text if email_elem is not None and "@" in email_elem.text else "N/A"

        papers.append(paper_data)

    return papers
