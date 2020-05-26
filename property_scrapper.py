
import utils_scrapper as utils

def scrap_property_to_dict(prop):
    d = {}

    d['Address'] = utils.scrap_safe_text(prop.find_all('span', {'class': 'propAddressCollapse'})[0])
    d['Locality'] = utils.scrap_safe_text(prop.find_all('span', {'class': 'propAddressCollapse'})[1])
    d['Price'] = utils.scrap_safe_text(prop.find('h4', {'class': 'propPrice'}))

    try:
        d['Beds'] = prop.find('span', {'class': 'infoBed'}).find('b').text
    except:
        d['Beds'] = None
        pass

    try:
        d['Area'] = prop.find('span', {'class': 'infoSqFt'}).find('b').text
    except:
        d['Area'] = None
        pass

    try:
        d['Full Baths'] = prop.find('span', {'class': 'infoValueFullBath'}).find('b').text
    except:
        d['Full Baths'] = None
        pass

    try:
        d['Half Baths'] = prop.find('span', {'class': 'infoValueHalfBath'}).find('b').text
    except:
        d['Half Baths'] = None
        pass

    for column_group in prop.find_all('div', {'class': 'columnGroup'}):
        for feature_group, feature_name in zip(column_group.find_all('span', {'class': 'featureGroup'}), column_group.find_all('span', {'class': 'featureName'})):
            if "Lot Size" in feature_group.text:
                d['Lot Size'] = feature_name.text

    return d
