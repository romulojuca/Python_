from datetime import date

ano = int (input('Digite o ano para saber se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('O ano {} é BISSEXTO'.format (ano))
else:
    print ('O ano {} não é BISSEXTO'.format (ano))
