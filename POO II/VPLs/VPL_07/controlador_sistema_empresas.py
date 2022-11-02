from empresa_dao import EmpresaDAO
from empresa_duplicada_exception import EmpresaDuplicadaException
from empresa import Empresa


class ControladorSistemaEmpresas():
    
    def __init__(self):
        self.__dao = EmpresaDAO()

    '''
    Permite incluir uma empresa utilizando a EmpresaDAO. 
    Valida pelo CNPJ se a empresa ja esta cadastrada
    Utiliza a EmpresaDAO para buscar as empresas
    @param empresa objeto Empresa que sera incluido
    @throws EmpresaDuplicadaException Excecao gerada quando se
    tenta incluir uma empresa com CNPJ ja cadastrado
    '''
    def inclui_empresa(self, empresa: Empresa):
        if self.busca_empresa_pelo_cnpj(empresa.cnpj) is not None:
            raise EmpresaDuplicadaException
        else:
            self.__dao.add(empresa)

    '''
    Permite excluir uma empresa cadastrada na EmpresaDAO
    @param empresa empresa que sera excluida
    '''
    def exclui_empresa(self, empresa: Empresa):
        if self.busca_empresa_pelo_cnpj(empresa.cnpj) is not None:
            self.__dao.remove(empresa)


    '''
    Permite buscar uma empresa na lista de empresas pelo CNPJ
    Utiliza a EmpresaDAO para buscar as empresas
    @param cnpj numero do CNPJ da empresa desejada
    @return retorna None se a empresa nao for encontrada
    '''
    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        return self.__dao.get(cnpj)

    '''
    Retorna a lista de empresas cadastradas
    Utiliza a EmpresaDAO para buscar as empresas
    @return lista de empresas cadastradas
    '''
    @property
    def empresas(self) -> list:
        return self.__dao.get_all()

    '''
    Calcula o total de impostos de todas as empresas.
    Invoca a operacao total_impostos() de cada uma
    das empresas cadastradas no Dicionario, somando os resultados
    Utiliza a EmpresaDAO para buscar as empresas
    @return somatorio dos impostos de todas as empresas cadastradas
    '''
    def calcula_total_impostos(self) -> float:
        total = 0
        for empresa in self.empresas:
            total += empresa.total_impostos()
        return total
        