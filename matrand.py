import numpy as np


def gerador(N):
    """
    Gera uma matriz aleatória N-por-N apenass com valores 0 e 1.

    Args:
        N (int): dimensão da matriz.

    Returns:
        M (np.array): matriz aleatória N-por-N.
    """

    ########################
    #### Completar aqui ####
    ########################
    
    return M



def media(M):
    """
    Calcula a média sobre todos os elementos da matriz.

    Args:
        M (np.array): matriz aleatória N-por-N.

    Returns:
        media (float): média sobre todos os elementos da matriz.
    """

    ########################
    #### Completar aqui ####
    ########################
    
    return media



if __name__ == "__main__":
    N = 10
    M = gerador(N)
    print("A matriz gerada é:\n",M)
    print("A sua média é:",media(M))
