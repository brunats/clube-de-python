import datetime


class FluxoCondicional(object):
    """docstring for FluxoCondicional."""

    def __init__(self, arg):
        super(FluxoCondicional, self).__init__()
        self.arg = arg

    def ehMaiorDeIdade(diaNascimento, mesNascimento, anoNascimento){
        idade = self._calculaIdade(diaNascimento, mesNascimento, anoNascimento)

        if idade.year > 18:
            return True
        return False
    }

    def _calculaIdade(dia, mes, ano){
        idade = datetime.date(day=dia, month=mes, year=ano) - datetime.datetime.now()
        return idade
    }
