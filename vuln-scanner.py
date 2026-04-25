import requests

url = input("Enter website URL (with http/https): ")

print("\nChecking security headers...\n")

try:
    response = requests.get(url)
    headers = response.headers

    # Security Headers Check
    if "X-Frame-Options" not in headers:
        print("❌ Missing X-Frame-Options (Clickjacking risk)")

    if "Content-Security-Policy" not in headers:
        print("❌ Missing Content-Security-Policy (XSS risk)")

    if "Strict-Transport-Security" not in headers:
        print("❌ Missing HSTS (HTTPS not enforced)")


    # 🔥 SQL Injection Test
    print("\nTesting SQL Injection...")

    payload = "' OR '1'='1"
    test_url = url + "?id=" + payload

    try:
        res = requests.get(test_url)
        if "error" in res.text.lower():
            print("⚠️ Possible SQL Injection vulnerability")
    except:
        pass


    # ⚡ XSS Test
    print("\nTesting XSS...")

    xss_payload = "<script>alert(1)</script>"
    test_url = url + "?q=" + xss_payload

    try:
        res = requests.get(test_url)
        if xss_payload in res.text:
            print("⚠️ Possible XSS vulnerability")
    except:
        pass


    print("\nScan complete ✅")

except:
    print("Error connecting to website")