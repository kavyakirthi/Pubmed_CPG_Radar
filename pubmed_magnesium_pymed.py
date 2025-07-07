from pymed import PubMed

pubmed = PubMed(tool="MyTool", email="kavya.kirthi1001@example.com")

query = "Magnesium"
results = pubmed.query(query, max_results=10)

for idx, article in enumerate(results, 1):
    title = article.title or "No title available."
    
    authors = []
    for author in article.authors:
        firstname = author.get("firstname", "")
        lastname = author.get("lastname", "")
        if firstname or lastname:
            authors.append(f"{firstname} {lastname}".strip())
    if not authors:
        authors = ["No authors listed"]
    first_two_authors = authors[:2]
    journal = article.journal or "No journal info"
    pub_date = article.publication_date
    if pub_date:
        pub_date_str = pub_date.strftime("%B %d, %Y") if hasattr(pub_date, 'strftime') else str(pub_date)
    else:
        pub_date_str = "No publication date"

    abstract_text = article.abstract
    if abstract_text:
       
        abstract_sentences = [s.strip() for s in abstract_text.split(". ") if s.strip()]
        if len(abstract_sentences) >= 2:
            short_abstract = ". ".join(abstract_sentences[:2]) + "."
        else:
            short_abstract = abstract_text.strip()
            if not short_abstract.endswith('.'):
                short_abstract += '.'
    else:
        short_abstract = "No abstract available."

    print(f"Title: {title}")
    print(f"Authors: {', '.join(first_two_authors)}")
    print(f"Journal: {journal}")
    print(f"Publication Date: {pub_date_str}")
    print(f"Abstract: {short_abstract}")
    print("-" * 80)
