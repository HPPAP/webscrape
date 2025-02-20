import requests
import multiprocessing
import time

volumes = [
    ["chi.16586151", "v.2 1640-42", "1148"],
    ["chi.18173921", "v.3 1642-44", "854"],
    ["chi.18173825", "v.4 1644-46", "758"],
    ["chi.31110057", "v.5 1646-48", "714"],
    ["mdp.39015056729323", "v.5 1646-1648", "802"],
    ["chi.16416294", "v.6 1648-51", "716"],
    ["mdp.39015056729315", "v.6 1648-1651", "714"],
    ["chi.18173849", "v.7 1651-59", "988"],
    ["chi.099164142", "v.8-11 1660-97 index", "1086"],
    ["chi.48502872", "v.8 1660-67", "708"],
    ["chi.19251911", "v.9 1667-87", "848"],
    ["chi.22692473", "v.9 1699-1703", "966"],
    ["mdp.39015056560777", "v.10 1688-1693", "910"],
    ["chi.56931621", "v.11 1693-1697", "848"],
    ["mdp.39015056560686", "v.12 1697-1699", "716"],
    ["chi.20670875", "v.13 1699-1702", "920"],
    ["mdp.39015056560520", "v.15 1705-1708", "698"],
    ["umn.31951d02551121t", "v.16 (1708/11)", "710"],
    ["mdp.39015056560678", "v.16 1708-1711", "702"],
    ["chi.22690202", "v.17 1711-14", "772"],
    ["umn.31951d01721987f", "v.18/34 1714/74", "1024"],
    ["chi.39697822", "v.18-34 1714-74 index", "1006"],
    ["umn.31951d02551123p", "v.18 (1714/17)", "786"],
    ["mdp.39015056560801", "v.18 1714-1718", "808"],
    ["chi.78147367", "v.19 1718-21", "816"],
    ["mdp.39015056560660", "v.19 1718-1721", "818"],
    ["chi.42850273", "v.21 1727-32", "1010"],
    ["chi.78147514", "v.23 1737-41", "766"],
    ["mdp.39015056560504", "v.23 1737-1741", "770"],
    ["chi.78147069", "v.24 1741-45", "944"],
    ["chi.20806722", "v.26 1750-54", "1074"],
    ["chi.20806657", "v.27 1754-57", "980"],
    ["chi.78147312", "v.30 1765-66", "896"],
    ["chi.78147507", "v.31 1766-67", "708"],
    ["mdp.39015056564506", "v.31 1766-1768", "726"],
    ["chi.78147083", "v.32 1768-70", "1034"],
    ["chi.78147141", "v.33 1770-72", "1008"],
    ["chi.78147261", "v.34 1772-74", "868"],
    ["chi.74591227", "v.35-55 1774-1800 index", "886"],
    ["chi.78147329", "v.35 1774-76", "866"],
    ["chi.78147374", "v.37 1778-1780", "996"],
    ["chi.78147432", "v.38 1780-82", "1216"],
    ["chi.78147381", "v.40 1784-85", "1228"],
    ["chi.78147449", "v.41 1786", "1020"],
    ["chi.78146571", "v.42 1787", "894"],
    ["chi.78147045", "v.43 1787-88", "694"],
    ["chi.099164312", "v.44 1788-89", "688"],
    ["mdp.39015016370515", "v.44 1788-1789", "688"],
    ["chi.16855766", "v.47 1792", "1140"],
    ["chi.78146622", "v.48 1792-1793", "1050"],
    ["mdp.39015056730933", "v.49 1794", "790"],
    ["mdp.39015056730925", "v.50 1794-1795", "694"],
    ["chi.099164370", "v.51 1796", "842"],
    ["chi.099164388", "v.52 1796-97", "814"],
    ["chi.099164396", "v.53 1797-98", "752"],
    ["mdp.39015056730750", "v.53 1797-1798", "754"],
    ["chi.78146608", "v.54 1798-99", "794"],
    ["chi.41856726", "v.56-75 1801-20 index", "1100"],
    ["iau.31858029589490", "v.59 1805/06", "852"],
    ["chi.099164485", "v.62 1805-06", "1058"],
    ["chi.099164493", "v.63 1808-09", "1008"],
    ["mdp.39015056730867", "v.64 1809", "766"],
    ["mdp.39015056730859", "v.65 1819", "864"],
    ["chi.63763646", "v.66 1810-11", "752"],
    ["chi.099164566", "v.70 1814-16", "1142"],
    ["mdp.39015056577557", "v.91 1836", "1026"],
    ["mdp.39015056577847", "v.92 1837", "840"],
    ["mdp.39015056577839", "v.93 1838", "1054"],
    ["mdp.39015056577821", "v.94 1839", "742"],
    ["chi.099164689", "v.95 1840", "850"],
    ["mdp.39015056577813", "v.95 1840", "852"],
    ["mdp.39015056577995", "v.96 1841", "778"],
    ["mdp.39015056577979", "v.98 1843", "800"],
    ["chi.099164728", "v.99 1844", "812"],
    ["mdp.39015056577961", "v.99 1844", "814"],
    ["uc1.c0000032052", "v.010 yr.1688/1693", "908"],
    ["uc1.c0000029595", "v.026 yr.1754", "1074"],
    ["uc1.c0000029488", "v.027 yr.1757", "978"],
    ["uc1.c0000032193", "v.029 yr.1764", "1120"],
    ["uc1.c0000032250", "v.036 yr.1776/1778", "1066"],
    ["uc1.c0000032284", "v.040 yr.1785", "1230"],
    ["uc1.c0000035311", "INDEX: v.056-075 yr.1800-1820", "1094"],
    ["uc1.c0000032607", "v.072 yr.1817", "944"],
    ["uc1.c0000032623", "v.074 yr.1819", "1280"],
    ["uc1.c0000032649", "v.076 yr.1821", "1424"],
    ["uc1.c0000029876", "v.082 yr.1827", "1062"],
    ["uc1.e0000056663", "v.092 yr.1837", "850"],
    ["uc1.e0000056671", "v.093 yr.1837/1838", "1066"],
    ["uc1.e0000056689", "v.094 yr.1839", "746"],
    ["uc1.e0000056705", "v.096 yr.1841", "782"],
    ["chi.099164736", "v.100 1845", "1138"],
    ["mdp.39015056577953", "v.100 1845", "1138"],
    ["chi.099164744", "v.101 pt.1 1846", "806"],
    ["uc1.e0000056762", "v.101 pt.2 yr.1846", "784"],
    ["chi.099164752", "v.101 pt.2 1846-47", "784"],
    ["mdp.39015056577805", "v.101 1846-1847 pt.1", "818"],
    ["mdp.39015056577797", "v.101 1846-1847 pt.2", "778"],
    ["chi.099164760", "v.102 1847", "1182"],
    ["mdp.39015056577946", "v.102 1847", "1200"],
    ["mdp.39015056577789", "v.103 1847-1848", "1220"],
    ["mdp.39015056577938", "v.104 1848-1850", "740"],
    ["uc1.e0000056804", "v.105 yr.1850", "804"],
    ["chi.099164809", "v.106 1851-52", "576"],
    ["mdp.39015056577771", "v.106 1851-1852", "572"],
    ["mdp.39015056577763", "v.107 1852", "476"],
    ["chi.099164972", "v.108-120 1852-65 index", "1052"],
    ["chi.099164859", "v.108 1852-54", "1004"],
    ["mdp.39015056577912", "v.108 1852-1854", "1010"],
    ["chi.099164867", "v.109 1854", "626"],
    ["mdp.39015056577755", "v.109 1854", "630"],
    ["chi.099164875", "v.110 1854-55", "600"],
    ["mdp.39015056577904", "v.110 1854-1855", "600"],
    ["chi.099164883", "v.111 1856", "508"],
    ["mdp.39015056577748", "v.111 1856", "514"],
    ["chi.099164891", "v.112 1857", "574"],
    ["mdp.39015056577896", "v.112 1857", "574"],
    ["mdp.39015056577730", "v.113 1857-1859", "488"],
    ["uc1.e0000056895", "v.114 yr.1859", "520"],
    ["mdp.39015056577888", "v.114 1859", "524"],
    ["uc1.e0000056903", "v.115 yr.1860", "652"],
    ["mdp.39015056577722", "v.115 1860-1861", "648"],
    ["mdp.39015056577870", "v.116 1861-1862", "558"],
    ["mdp.39015056577714", "v.117 1862-1863", "514"],
    ["mdp.39015056577862", "v.118 1863-1864", "540"],
    ["mdp.39015056577706", "v.120 1865", "592"],
    ["chi.74591169", "v.121-134 1866-1878/79 index", "1162"],
    ["mdp.39015056578142", "v.121 1865-1867", "684"],
    ["uc1.e0000056978", "v.122 yr.1867", "604"],
    ["mdp.39015056578134", "v.122 1867", "608"],
    ["uc1.e0000056986", "v.123 yr.1867/1868", "498"],
    ["mdp.39015056578126", "v.123 1867-1868", "500"],
    ["mdp.39015056578118", "v.124 1868-1869", "550"],
    ["mdp.39015056731386", "v.125 1870", "546"],
    ["uc1.e0000057018", "v.126 yr.1877", "578"],
    ["mdp.39015056731394", "v.126 1871", "586"],
    ["uc1.e0000057026", "v.127 yr.1872", "570"],
    ["mdp.39015056733242", "v.127 1872", "580"],
    ["mdp.39015056732947", "v.128 1873", "572"],
    ["mdp.39015056733093", "v.129 1874", "514"],
    ["mdp.39015056732939", "v.130 1875", "598"],
    ["uc1.e0000057067", "v.131 yr.1876", "564"],
    ["mdp.39015056732921", "v.131 1876", "568"],
    ["mdp.39015056732913", "v.132 1877", "590"],
    ["uc1.e0000057083", "v.133 yr.1878", "580"],
    ["mdp.39015056732905", "v.133 1878", "588"],
    ["uc1.e0000057091", "v.134 yr.1878/1879", "586"],
    ["mdp.39015056732897", "v.134 1878-1879", "594"],
    ["uc1.e0000057109", "v.135 yr.1860", "610"],
    ["chi.099165106", "v.135 1880", "614"],
    ["mdp.39015056733085", "v.135 1880", "612"],
    ["mdp.39015056733077", "v.136 1881", "676"],
    ["mdp.39015056733069", "v.137 1882", "722"],
    ["mdp.39015056732889", "v.138 1883", "658"],
    ["mdp.39015056733051", "v.139 1884", "634"],
    ["mdp.39015056732871", "v.140 1884-1885", "572"],
    ["chi.099165156", "v.140 1885", "570"],
    ["mdp.39015056732863", "v.141 1886", "562"],
    ["uc1.e0000057174", "v.142 yr.1887", "716"],
    ["mdp.39015056732855", "v.142 1887", "724"],
    ["uc1.e0000057182", "v.143 yr.1888", "706"],
    ["chi.099165237", "v.147 1892", "596"],
    ["mdp.39015056732830", "v.147 1892", "612"],
    ["mdp.39015056733234", "v.148 1893-1894", "898"],
    ["mdp.39015056733226", "v.149 1894", "562"],
    ["mdp.39015056733218", "v.150 1895", "552"],
    ["mdp.39015056733200", "v.151 1896", "46"],
    ["chi.099165287", "v.152 1897", "596"],
    ["uc1.e0000057281", "v.153 yr.1898", "592"],
    ["mdp.39015056733184", "v.153 1898", "596"],
    ["mdp.39015056733176", "v.154 1899", "620"],
    ["mdp.39015056733168", "v.155 1900", "602"],
    ["chi.099165342", "v.157 1902", "706"],
    ["chi.099165350", "v.158 1903", "574"],
    ["chi.099165368", "v.159 1904", "576"],
    ["uc1.e0000059923", "v.161 yr.1906", "686"],
    ["uc1.e0000059931", "v.162 yr.1907", "614"],
    ["chi.099165407", "v.163 1908", "698"],
    ["chi.099165415", "v.164 1909", "710"],
    ["chi.099165423", "v.165 1910", "456"],
    ["uc1.c109614531", "Index v.166-175", "574"],
    ["chi.099165449", "v.166 1911", "696"],
    ["uc1.e0000059980", "v.167 yr.1912/1913", "730"],
    ["chi.099165465", "v.168 1913", "496"],
    ["chi.099165473", "v.169 1914", "632"],
    ["uc1.e0000060012", "v.170 yr.1914/1916", "436"],
    ["chi.099165481", "v.170 1915", "436"],
    ["chi.099165499", "v.171 1916", "332"],
    ["chi.099165504", "v.172 1917", "388"],
    ["uc1.e0000060038", "v.172 yr.1917/1918", "388"],
    ["chi.099165512", "v.173 1918", "320"],
    ["chi.099165520", "v.174 1919", "516"],
    ["chi.099165538", "v.175 1920", "600"],
    ["chi.099165554", "v.176 1921", "488"],
    ["chi.099165619", "v.182 1927", "462"],
    ["chi.099165627", "v.183 1928", "388"],
    ["chi.099165635", "v.184 1929", "340"],
    ["uc1.e0000060194", "v.188 yr.1932/1933", "402"],
    ["uc1.e0000060202", "v.189 yr.1933/1934", "422"],
    ["uc1.e0000060210", "v.190 yr.1934/1935", "416"],
    ["uc1.e0000060228", "v.191 yr.1935/1936", "448"],
    ["uc1.e0000060236", "v.192 yr.1936/1937", "474"],
    ["uc1.e0000060244", "v.193 yr.1937/1938", "484"],
    ["uc1.e0000060251", "v.194 yr.1938/1939", "564"],
    ["uc1.e0000060269", "v.195 yr.1939/1940", "310"],
    ["uc1.e0000060277", "v.196 yr.1940/1941", "248"],
    ["uc1.e0000060285", "v.197 yr.1941/1942", "218"],
    ["uc1.e0000060293", "v.198 yr.1942/1943", "230"],
    ["uc1.e0000060301", "v.199 yr.1943/1944", "262"],
    ["chi.63719499", "1714-1718", "826"],
]


def download_txt_file(url, filepath):
    """
    Downloads a .txt file from a URL and saves it to a specified filepath.

    Args:
        url (str): The URL of the .txt file to download.
        filepath (str): The local filepath to save the downloaded file.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except IOError as e:
        print(f"Error writing file: {e}")


def scrape(volume):
    id = volume[0]
    name = volume[1]
    l = int(volume[2])
    for i in range(l + 1):
        url = f"https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id={id}&attachment=1&tracker=D1&seq={i}"
        save_path = f"data/{id}-{name}-{i}.txt"
        download_txt_file(url, save_path)
        time.sleep(1)


# def main():
#     for volume in volumes:
#         id = volume[0]
#         for i in range(int(volume[2]) + 1):
#             url = f"https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id={id}&attachment=1&tracker=D1&seq={i}"
#             save_path = f"data/{id}-{volume[1]}-{i}.txt"
#             download_txt_file(url, save_path)


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(scrape, volumes)
    # href = "//babel.hathitrust.org/cgi/pt?id=uc1.c109614452"
    # txt_url = "https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id=chi.16586151&attachment=1&tracker=D1&seq=15"
    # txt_ur0 = "https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id=uc1.e0000060251&attachment=1&tracker=D1&seq=8"
    # txt_ur1 = "https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id=uc1.c109614452&attachment=1&tracker=D1&seq=10"

    # save_path = "1.txt"
    # download_txt_file(txt_url, save_path)
    # main()


# https://babel.hathitrust.org/cgi/imgsrv/download/plaintext?id=chi.16586151&attachment=1&tracker=D1&seq=12
