from bs4 import BeautifulSoup

html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
<body>

	<p class="title">
		<b>The Dormouse's story</b>
	</p>

	<p class="story">Once upon a time there were three little sisters; and their names were
		<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
		<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.
	</p>

</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

first_p = soup.find('p')
print(first_p)
# now this first_p becomes a soup object which can be used to search for further content inside it

print(first_p.find('a'))
print(first_p.find('b'))