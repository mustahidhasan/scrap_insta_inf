from app import handler


def main():
    """
    This function is used to call the handler function.
    :return:
    """
    url_list_to_scrape = [
        {"url": "https://www.instagram.com/", "keyword": ["robertdowneyjr/"], "function": "get_insta_inf_info"}, # to send the event to the hotpapper scrape function

    ]
    for url_list_elem in url_list_to_scrape:
        if "keyword" in url_list_elem:
            for keyword_item in url_list_elem["keyword"]:
                event = {
                    "login_url": url_list_elem.get("login_url", None),
                    "url": url_list_elem["url"],
                    "function": url_list_elem["function"],
                    "keyword": keyword_item
                }
                handler(event, {})
        else:
            event = {
                "login_url": url_list_elem.get("login_url", None),
                "url": url_list_elem["url"],
                "function": url_list_elem["function"],
            }
            handler(event, {})


if __name__ == '__main__':
    main()