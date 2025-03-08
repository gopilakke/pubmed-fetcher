import argparse
import csv
from pubmed_fetcher.fetch import fetch_pubmed_papers, fetch_paper_details

def save_to_csv(papers, filename="pubmed_papers.csv"):
    """Save fetched papers to a CSV file."""
    if not papers:
        print("No data to save.")
        return
    
    keys = papers[0].keys()  # Get column names from dictionary keys
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(papers)

    print(f"\n✅ Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and export to CSV")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("--output", type=str, default="pubmed_papers.csv", help="Output CSV file name")
    
    args = parser.parse_args()

    print(f"Fetching papers for query: {args.query}...")
    paper_ids = fetch_pubmed_papers(args.query)

    if not paper_ids:
        print("No papers found.")
        return

    papers = fetch_paper_details(paper_ids)

    if not papers:
        print("No detailed data found.")
        return

    # Print results
    for paper in papers:
        print(f"\n🔹 Title: {paper['Title']}")
        print(f"   📄 PubMed ID: {paper['PubmedID']}")
        print(f"   👨‍🔬 Authors: {paper['Authors']}")
        print(f"   🏢 Company Affiliations: {paper['Company Affiliations']}")
        print(f"   📧 Corresponding Author Email: {paper['Corresponding Author Email']}")

    # Save to CSV
    save_to_csv(papers, args.output)

if __name__ == "__main__":
    main()
