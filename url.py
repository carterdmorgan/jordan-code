import hashlib

class URL:
    # key: long_url, value: URL()
    URL_DICT = {}

    def __init__(self, long_url: str) -> None:
        self.long_url = long_url
        self.short_url = "short_url"
        self.access_count = 0

    def shorten_url(long_url):
        if long_url.startswith('www.') is False:
            raise ValueError
              
        url_check = URL.URL_DICT.get(long_url)

        if url_check is not None:
            return getattr(url_check, 'short_url')
        elif url_check is None:
            new_url_obj = URL(long_url)

            # hash long_url to create unique short_url
            hash_obj = hashlib.shake_256(long_url.encode())
            short_url = hash_obj.hexdigest(3)
            new_url_obj.short_url = str(short_url)
            URL.URL_DICT[long_url] = new_url_obj
            return new_url_obj.short_url
        
    def get_long_url(short_url: str):
        url_obj = None

        for key, obj in URL.URL_DICT.items():
            if getattr(obj, 'short_url') == short_url:
                url_obj = obj
                break

        if url_obj is None:
            raise ValueError
        elif url_obj is not None:
            url_obj.access_count += 1
            return url_obj.long_url
        
    def get_access_count(short_url: str):
        url_obj = None

        for key, obj in URL.URL_DICT.items():
            if getattr(obj, 'short_url') == short_url:
                url_obj = obj
                break
        if url_obj is not None:
            return getattr(url_obj, 'access_count')
        elif url_obj is None:
            raise ValueError
    
def main():
    my_url = URL('www.homestarrunner.com').long_url
    my_short_url = URL.shorten_url(my_url)
    print(my_short_url)
    print(URL.get_long_url(my_short_url))
    print(URL.get_access_count(my_short_url))
    print('End of line')
main()