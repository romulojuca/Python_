from uteis import sifrao


def metade(v=0, formato=False):
    resp = v / 2
    return resp if formato is False else sifrao.moedabr(resp)


def dobro(v=0, formato=False):
    resp = v * 2
    return resp if formato is False else sifrao.moedabr(resp)


def aumentar_percentual(v=0, percentual=0, formato=False):
    resp = v + (percentual / 100 * v)
    return resp if formato is False else sifrao.moedabr(resp)


def diminuir_percentual(v=0, percentual=0, formato=False):
    resp = v - (percentual / 100 * v)
    return resp if formato is False else sifrao.moedabr(resp)


def resumo(v=0, perc_aum=0, perc_dim=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analizado: {sifrao.moedabr(v)}')
    print(f'Dobro é: {dobro(v, True):>17}')
    print(f'Metade é: {metade(v, True):>15}')
    print(f'{perc_aum}% de aumento: {aumentar_percentual(v, True):>7}')
    print(f'{perc_dim}% de redução: {diminuir_percentual(v, True):>6}')
    print('-' * 30)
