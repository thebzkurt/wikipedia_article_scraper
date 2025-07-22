import requests
from bs4 import BeautifulSoup

# Step 1: Get wikipedia article url
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ','_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code:{response.status_code}. Check the topic and try again")
        return None

# Step 2: Extract article title
def extract_title(soup):
    return soup.find('h1').text

# Step 3: Extract article summary
def extract_summary(soup):
    paragraphs = soup.find_all('p')
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No summary found"

# Step 4: Extract headings
def extract_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
    return headings

# Step 5: Extract related links
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org/wiki/{href}")
    return list(set(links))[:10]

# Step 6: Main program
def main():
    topic = input("Enter a topic to search on wiki: ").strip()
    page_content = get_wikipedia_page(topic)

    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = extract_title(soup)
        summary = extract_summary(soup)
        headings = extract_headings(soup)
        related_links = get_related_links(soup)

        print("\n---- Wikipedia Article Details ----")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")
        print("\nHeading")
        for hding in headings:
            print(f"- {hding}")

        print("\nReladed Links")
        for link in related_links:
            print(f"- {link}")

if __name__ == "__main__":
    main()


