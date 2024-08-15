# Compilar a biblioteca de Ray Tracing
all: build run

build:
    gcc -shared -o raytracing.so -fPIC raytracing.c

# Executar o programa Python
run:
    python3 main.py

# Limpar os arquivos gerados
clean:
    rm -f raytracing.so
