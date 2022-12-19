import re
urls = []
text = input()
while text:
    matched = re.finditer(r"(?P<url>www\.[A-Za-z0-9-]+(\.[a-z]+)+)", text)

    if matched:

        for url in matched:
            urls.append(url.group("url"))
    text = input()
for elements in urls:
    print("".join(elements))