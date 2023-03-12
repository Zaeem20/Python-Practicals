import re
import urllib.request as ur


request = ur.Request(r'file:///D://Python-Practicals//regex//x.html')
with ur.urlopen(request) as resp:
    page = resp.read()

    pattern = r'\w+@\w+\.(?:com|in|net)'  # Email Regex
    result = re.findall(pattern, page.decode('utf-8'))
    print("Emails Found:", ''.join(result))


print("Coded By Durani Mohammed Zaeem; Roll no: 425")

# written by Durani Mohammed Zaeem Abdul Qadir