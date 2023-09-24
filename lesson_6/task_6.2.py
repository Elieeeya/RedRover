XPATH_1 = "//p[contains(text(),'Fully charged cat')]"
XPATH_2 = "//p[@class='card-text' and text()='Fully charged cat']"
XPATH_3 = "//div//p[contains(text(),'Fully charged cat')]"

CSS_1 = "body > main > div > div > div > div:nth-child(5) > div > div > p"
CSS_2 = "p.card-text[xpath='1']"
CSS_3 = ".card p.card-text[xpath='1']"