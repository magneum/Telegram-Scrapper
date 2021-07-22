from Liters import *

def pre_user_app(stel_token):
    """scraps the web page using the provided cookie,
    returns True or False appropriately"""
    request_url = "https://my.telegram.org/apps"
    custom_header = {
        "Cookie": stel_token
    }
    response_c = requests.get(request_url, headers=custom_header)
    response_text = response_c.text
    print(response_text)
    soup = BeautifulSoup(response_text, features="html.parser")
    title_of_page = soup.title.string
    re_dict_vals = {}
    re_status_id = None
    if "configuration" in title_of_page:
        print(soup.prettify())
        g_inputs = soup.find_all("span", {"class": "input-xlarge"})
        app_id = g_inputs[0].string
        api_hash = g_inputs[1].string
        test_configuration = g_inputs[4].string
        production_configuration = g_inputs[5].string
        _a = "It is forbidden to pass this value to third parties."
        hi_inputs = soup.find_all("p", {"class": "help-block"})
        test_dc = hi_inputs[-2].text.strip()
        production_dc = hi_inputs[-1].text.strip()
        re_dict_vals = {
            "App Configuration": {
                "app_id": app_id,
                "api_hash": api_hash
            },
            "Available MTProto Servers": {
                "test_configuration": {
                    "IP": test_configuration,
                    "DC": test_dc
                },
                "production_configuration": {
                    "IP": production_configuration,
                    "DC": production_dc
                }
            },
            "Disclaimer": _a
        }
        #
        re_status_id = True
    else:
        tg_app_hash = soup.find("input", {"name": "hash"}).get("value")
        re_dict_vals = {
            "tg_app_hash": tg_app_hash
        }
        re_status_id = False
    return re_status_id, re_dict_vals
