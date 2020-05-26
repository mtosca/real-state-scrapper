
def scrap_safe_text(element):
    if element == None:
        return ""

    return element.text.strip()

def scrap_safe_integer(element):
    if element == None:
        return 0
    
    try:
        return int(element.text)
    except:
        return 0