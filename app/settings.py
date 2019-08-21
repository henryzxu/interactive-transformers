data_dir = 'app/data'
output_dir = 'app/results'
PORT = 8080
gen_file = "app/data/squad_input.json"

http_proxy = ""
https_proxy = ""

if http_proxy or https_proxy:
    proxyDict = {
                  "http": http_proxy,
                  "https": https_proxy,
                }
else:
    proxyDict = {}
