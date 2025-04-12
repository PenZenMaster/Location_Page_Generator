# page_generator.py

import os
import csv
from slugify import slugify
from jinja2 import Template

# Define your HTML template (load from a separate file or embed inline for now)
HTML_TEMPLATE = """
<!-- {{ location }} Location Page – {{ business_name }} -->

<h1>{{ page_title }}</h1>
<p>{{ intro_paragraph }}</p>

<a title="{{ image_attribution }}" href="{{ image_source_url }}" target="_blank" rel="noopener">
  <img width="100%" style="height:auto; margin: 20px 0;" src="{{ image_embed_url }}" alt="{{ page_title }}">
</a>

<h2>Why Choose {{ page_title }} from {{ business_name }}?</h2>
<p>{{ why_us_paragraph }}</p>

<h2>Explore {{ location }} While We Work</h2>
<p>{{ local_paragraph }}</p>
<iframe src="{{ map_embed_url }}" width="100%" height="400" style="border:0;" allowfullscreen loading="lazy"></iframe>

<h2>Driving Directions to Our Office from {{ location }}</h2>
<p>We're located at {{ hq_address }}.</p>
<iframe src="{{ directions_embed_url }}" width="100%" height="400" style="border:0;" allowfullscreen loading="lazy"></iframe>

<h2>Exterior Painting Services We Offer in {{ location }}</h2>
<ul>
  {% for service in services %}
  <li>{{ service }}</li>
  {% endfor %}
</ul>

<h2>Request a Free Quote Today</h2>
<p>{{ cta_paragraph }}</p>
<p><strong>Contact Us:</strong><br>
Phone: <a href="tel:{{ phone }}">{{ phone }}</a><br>
Email: <a href="mailto:{{ email }}">{{ email }}</a><br>
Address: <a href="{{ hq_map_url }}" target="_blank">{{ hq_address }}</a></p>
"""

# Sample services list
DEFAULT_SERVICES = [
    "Full exterior repaints",
    "Trim, fascia, shutters, and doors",
    "Deck and porch painting or staining",
    "Color consultation",
    "Historic restoration or modern upgrades",
]


# Main generator function
def generate_location_page(row):
    focus_keyword = row["Primary Focus Keyword"]
    location = row["Location"]
    phone = row["Phone"]
    email = row["Email"]
    business_name = row["Business Name"]
    hq_address = row["HQ Address"]

    page_title = f"{focus_keyword} in {location}"
    slug = slugify(location)

    template = Template(HTML_TEMPLATE)
    html_output = template.render(
        page_title=page_title,
        business_name=business_name,
        location=location,
        phone=phone,
        email=email,
        hq_address=hq_address,
        hq_map_url="https://goo.gl/maps/kD8T7YAkzEv6GQbC8",
        map_embed_url="https://www.google.com/maps/embed?...",  # placeholder
        directions_embed_url="https://www.google.com/maps/embed?...",  # placeholder
        image_embed_url="https://upload.wikimedia.org/...jpg",  # placeholder
        image_source_url="https://commons.wikimedia.org/wiki/...",  # placeholder
        image_attribution="Photographer, CC License, via Wikimedia Commons",
        intro_paragraph=f"Professional {focus_keyword.lower()} with guaranteed reliability and clean, lasting results.",
        why_us_paragraph="Our proven process includes power washing, priming, and expert application using top-tier materials.",
        local_paragraph=f"Enjoy local favorites in {location} while we handle the hard work—like coffee downtown or time in the park.",
        cta_paragraph=f"Looking for {focus_keyword.lower()} you can trust in {location}? Let's talk!",
        services=DEFAULT_SERVICES,
    )

    output_path = os.path.join("output", f"{slug}.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"✅ Generated: {output_path}")


# Load CSV and process each row
def run():
    with open("input/locations.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            generate_location_page(row)


if __name__ == "__main__":
    run()
