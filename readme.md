# Ray Tracing em Python e C

Este projeto implementa um simples algoritmo de Ray Tracing utilizando Python para a interface do usuário e C para os cálculos de Ray Tracing.

## Estrutura do Projeto

- `src/main.py`: Interface gráfica e execução do Ray Tracing.
- `src/raytracing.c`: Implementação do Ray Tracing em C.
- `src/binding.py`: Ligação entre Python e C.
- `Makefile`: Script para compilar e executar o projeto.

## Como Executar

1. Clone o repositório:
    ```
    git clone <URL do repositório>
    ```

2. Navegue até o diretório do projeto:
    ```
    cd raytracing-project/src
    ```

3. Compile o código C e execute o projeto:
    ```
    make
    ```

4. Limpe os arquivos gerados:
    ```
    make clean
    ```

## Requisitos

- Python 3.x
- GCC (compilador C)
- Bibliotecas Python: `numpy`, `PIL`, `tkinter`

## Documentação

Para mais detalhes sobre a implementação, consulte o arquivo `documentação.pdf`.
