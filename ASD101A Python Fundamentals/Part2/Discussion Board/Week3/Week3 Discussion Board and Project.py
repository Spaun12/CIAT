# Week 2 Discussion Board and Project Bones Michael Connell

# Ask the user for the county name and state
county_name = input("Enter the county name: ")
state = input("Enter the state abbreviation: ")

# Construct the URL for the website or database
url = "https://example.com/licenses/" + state + "/" + county_name

# Use a web scraping library (such as BeautifulSoup) to extract the relevant information
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("Error: Could not retrieve information for the specified county.")
else:
    soup = BeautifulSoup(response.content, "html.parser")
    licenses = {}

    # Use a dictionary to store the required licenses and permits
    for item in soup.find_all("li", class_="license"):
        license_name = item.find("a").get_text()
        licenses[license_name] = item.find("p").get_text()

    # Print the license information to the user
    print("The following licenses and permits are required for", county_name, "County:")
    for license_name, description in licenses.items():
        print("- " + license_name + ": " + description)
