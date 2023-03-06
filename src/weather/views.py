from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup as bs

def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    # print(url)
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    LANGUAGE = 'en-US,en;q=0.8'
    COOKIE = 'SL_G_WPT_TO=en; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; HSID=AOL8FX2ugcgf5j2BF; SSID=AIbkb95GdIIuKM5Fw; APISID=Oz0Unr6BhYoHSMEc/ApC28RRfkdG2XKBeD; SAPISID=fyZ5mVQEpwrkLFN-/ADZBoDhn1ePraJt0r; __Secure-1PAPISID=fyZ5mVQEpwrkLFN-/ADZBoDhn1ePraJt0r; __Secure-3PAPISID=fyZ5mVQEpwrkLFN-/ADZBoDhn1ePraJt0r; SID=TQgSyy8zGAS8-pWI3f4jp_eoGXNubxOMQWZqhw-kVqPoJsxIgVf4NarHcq222pbrn6jhVg.; __Secure-1PSID=TQgSyy8zGAS8-pWI3f4jp_eoGXNubxOMQWZqhw-kVqPoJsxIkAC3j99vd7kO15bnkjVgsA.; __Secure-3PSID=TQgSyy8zGAS8-pWI3f4jp_eoGXNubxOMQWZqhw-kVqPoJsxIK-2d2jEHSQQZzwmNd2P4dQ.; S=billing-ui-v3=q6D-Q-byOiGl-C56dvC5fFSSXXRa7pfd:billing-ui-v3-efe=q6D-Q-byOiGl-C56dvC5fFSSXXRa7pfd:antipasti_server_prod=U2K5HeoCgoak4l8AD0iUTD48A92mvKvPMaAIPwjqIPY; OTZ=6915940_32_32__32_; AEC=ARSKqsIhEfIuDgG8_ksbr2i-yVlPTr7a2gMKXX1s9uDZggM89UyLUxBi6Q; SEARCH_SAMESITE=CgQI2ZcB; NID=511=BLbBt9zeN2TSNK4FYmQFVlwyo2xrtu5J8wx06I9lCIuYH6SchLntg-nBA1xl-HkfXDnCfDgUKmtLxK5j4KapKSz26dYeGD8Dq_B5w8YwVQcpMfrUY3P4-XpcxcGFL9Sxv3JdNoCyH7O-vXWvn1JrpCgXQInZq604lT9YRi9QkwjhOJ8l-UHr0oD0RwmmgZ6NjtYsl-Jp0wEKcP2vVuBIlB5FpBBNRnuKn_j-umkWJxh2ilRoRmpZmXJeTXQekJlv3wxoE2dVCuGobgDXeuto_fKKEcz8ixqoTrguWjXLL0wV01xXFJWwhUutXafznmzLQa-08I815lc0aSWf92lz-u8l0e8tZlGx6iCsPy6gGaH__lph063rh4vk9I-VlP5Z8oYg0ptBn16XlR_E_iQz4_eynaOjx391vgLz0wjdgn4dd3TYIHWyYQ-QCHkC18mK3wwcEOVhr_5U7p8NPmXIXtaKXAWBBERin4oTIrc; DV=Y8JruOLzMx-kUFfdruUpeWoFfxEualgvJBy_9Krq5AIAAPA1rd6NoN8y0wAAAAQWt4oXwIq_WQAAAAd64O4hw7ADFwAAAKHvbTNyUhyxst8AIBqkWuyFV2na7DcA8JIUD6qmhJJC-w0AeNTXKF8a5ELafgMApNQGsTWjdqK23wAA; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjc3NzY5OTM4MTc5MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDIzODE3NTAwMAogIGxvbmdpdHVkZV9lNzogOTA0MDk2MDAwCn0KcmFkaXVzOiA2MjAKcHJvdmVuYW5jZTogNgo=; 1P_JAR=2023-03-02-15; SIDCC=AFvIBn9zprkwil_PzkjuepOiQadIm5_a_6UADfRQVWJsLt_idOKAjwE9wBXPDTZj0bgJC1plWW8Y; __Secure-1PSIDCC=AFvIBn8ISlb2qHPENjNU5H-i7c5FpsIXWKkdq3X0Mt7ShDdbtz1UiOoCurfwGxwOgHTPKNl0ia6_; __Secure-3PSIDCC=AFvIBn8rsGV7QqIlDzNjGtzEBXg1aFLHCAkCqq0euR79KBdlDxQqaVBZEjUsln4Uo85re8S7dDs'
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    session.headers['cookie'] = COOKIE
    response = session.get(url)
    # print(response)
    soup = bs(response.text, 'html.parser')
    # Extract Location
    results = {}
    extract_location = soup.find("div", class_='eKPi4')
    results['region'] = extract_location.find_next('span', {'class' : 'BBwThe'}).text
    results['daytime'] = extract_location.find_next('div', attrs={'id' : 'wob_dts'}).text
    results['weather'] = extract_location.find_next('span', attrs={'id' : 'wob_dc'}).text
    results['temperature'] = extract_location.find_next('span', attrs={'id' : 'wob_tm'}).text
    # print(region)
    # print(day_time)
    # print(weather)
    # print(temperature)

    # return city
    print(results)
    return results


# get_weather_data('new york')
# Create your views here.
def home_view(request):
    if request.method == "GET" and 'city' in request.GET:
        city = request.GET.get('city')
        results = get_weather_data(city)
        context = {'results':results}
    else:
        context = {}

    return render(request, 'weather/home.html', context)



















