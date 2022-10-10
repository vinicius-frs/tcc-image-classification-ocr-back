import re

def extractDadosRGVerso(imageText):
    dados = {
        "rg": None,
        "nome": None,
        "naturalidade": None,
        "data_nascimento": None,
    }

    dados["rg"] = re.findall("\d{2}\.\d{3}\.\d{3}-[0-9X]", imageText["texts"][0])[0]

    nome_inicio = re.search("NOME|nome", imageText["texts"][0]).span()[1]
    nome_fim = re.search("FILIAÇÃO|filiação|FILIACAO|filiacao", imageText["texts"][0]).span()[0]
    dados["nome"] = imageText["texts"][0][nome_inicio:nome_fim].strip()

    naturalidade_inicio = re.search("NATURALIDADE|naturalidade", imageText["texts"][0]).span()[1]
    naturalidade_fim = re.search("DOC ORIGEM|doc origem", imageText["texts"][0]).span()[0]
    dados["naturalidade"] = imageText["texts"][0][naturalidade_inicio:naturalidade_fim].strip()

    data_nascimento_inicio = re.search("DATA DE NASCIMENTO|data de nascimento", imageText["texts"][0]).span()[1]
    dados["data_nascimento"] = re.findall("\d{2}\/\d{2}\/\d{4}", imageText["texts"][0][data_nascimento_inicio:len(imageText["texts"][0])])[0]

    return dados

def extractDadosCNHFrente(imageText):
    dados = {
        "rg": None,
        "cpf": None,
        "cnh": None,
        "nome": None,
        "cnh_validade": None,
        "data_nascimento": None,
    }

    rg_inicio = re.search("DOC IDENTIDADE/ORG. EMISSOR/UF", imageText["texts"][0]).span()[1]
    rg_fim = re.search("SSP", imageText["texts"][0]).span()[0]
    dados["rg"] = imageText["texts"][0][rg_inicio:rg_fim].strip()

    dados["cpf"] = re.findall("\d{3}\.\d{3}\.\d{3}-\d{2}", imageText["texts"][0])[0]

    cnh_inicio = re.search("NO REGISTRO-|NO REGISTRO", imageText["texts"][0]).span()[1]
    cnh_fim = re.search("DOC IDENTIDADE", imageText["texts"][0]).span()[0]
    dados["cnh"] = imageText["texts"][0][cnh_inicio:cnh_fim].strip()

    nome_inicio = re.search("NOME", imageText["texts"][0]).span()[1]
    nome_fim = re.search("NO REGISTRO", imageText["texts"][0]).span()[0]
    dados["nome"] = imageText["texts"][0][nome_inicio:nome_fim].strip()

    cnh_validade_inicio = re.search("VALIDADE", imageText["texts"][0]).span()[1] 
    cnh_validade_fim = re.search("ACC", imageText["texts"][0]).span()[0]
    dados["cnh_validade"] = re.findall("\d{2}\/\d{2}\/\d{4}", imageText["texts"][0][cnh_validade_inicio:cnh_validade_fim])[0]

    data_nascimento_inicio = re.search("DATA NASCIMENTO", imageText["texts"][0]).span()[1] 
    data_nascimento_fim = re.search("CPF", imageText["texts"][0]).span()[0]
    dados["data_nascimento"] = re.findall("\d{2}\/\d{2}\/\d{4}", imageText["texts"][0][data_nascimento_inicio:data_nascimento_fim])[0]

    return dados
    
def extractDadosCPFFrente(imageText):
    dados = {
        "cpf": None,
        "nome": None,
        "data_nascimento": None,
    }

    dados["cpf"] = re.findall("\d{3}\.\d{3}\.\d{3}-\d{2}", imageText["texts"][0])[0]

    nome_inicio = re.search("Nome", imageText["texts"][0]).span()[1]
    nome_fim = re.search("Nascimento", imageText["texts"][0]).span()[0]
    dados["nome"] = imageText["texts"][0][nome_inicio:nome_fim].strip()

    data_nascimento_inicio = re.search("Nascimento", imageText["texts"][0]).span()[1]
    dados["data_nascimento"] = re.findall("\d{2}\/\d{2}\/\d{4}", imageText["texts"][0][data_nascimento_inicio:len(imageText["texts"][0])])[0]

    return dados