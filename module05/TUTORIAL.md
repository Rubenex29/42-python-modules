# Tutorial Completo: Polimorfismo e Programação Orientada a Objetos

Este documento foi criado para te guiar, passo a passo, através dos conceitos fundamentais de programação orientada a objetos (POO) e, especificamente, **polimorfismo**, utilizando o código deste projeto como base.

Vamos começar do início, assumindo apenas o básico, e aprofundar à medida que avançamos nos exercícios.

---

## Parte 0: Revisão Relâmpago (O Básico)

Antes de falarmos de polimorfismo, vamos garantir que estamos na mesma página sobre o que são Classes e Objetos.

### O que é uma Classe?
Pensa numa classe como um **molde** ou uma **planta de arquitetura**. Ela define "o que é" alguma coisa, mas não é a coisa em si.
Exemplo: A planta de uma casa diz onde ficam as janelas, qual a cor da parede, etc.

### O que é um Objeto?
É a **instância** criada a partir do molde.
Exemplo: Se usares a planta para construir 3 casas, tens 3 objetos. Eles têm a mesma estrutura, mas podem ter dados diferentes (uma casa tem cortinas azuis, a outra vermelhas).

### Estrutura em Python:
```python
class Carro:  # O Molde
    def __init__(self, cor):
        self.cor = cor  # Atributo (característica)

    def andar(self):    # Método (ação)
        print("Vrum vrum!")

meu_carro = Carro("Vermelho") # O Objeto
meu_carro.andar() # Chama a ação
```

---

## Parte 1: O Que é Polimorfismo?

A palavra vem do grego: **Poly** (muitos) + **Morph** (formas).

Na programação, polimorfismo permite que **objetos de tipos diferentes sejam tratados da mesma maneira**.

**Analogia do Mundo Real:**
Imagina que tens um comando universal e um botão "Ligar".
- Se apontares para a TV e apertares "Ligar", a TV liga.
- Se apontares para o Ar Condicionado e apertares "Ligar", ele liga.
- Se apontares para a Playstation e apertares "Ligar", ela liga.

A ação é a mesma ("Ligar"), mas cada aparelho reage de forma diferente. Tu (o utilizador) não precisas saber *como* cada um liga, apenas que eles *sabem* ligar.

Isso é polimorfismo!

---

## Parte 2: Exercício 0 - A Fundação (DataProcessor)

Neste primeiro exercício, vamos ver o polimorfismo através de **Herança** e **Classes Abstratas**.

### Análise do Código (`ex0/stream_processor.py`)

#### 1. A Classe Abstrata (`DataProcessor`)
O código define uma classe especial chamada `DataProcessor` que herda de `ABC` (Abstract Base Class).

```python
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass
```

- **O que isso significa?** Esta classe é um **contrato**. Ela diz: "Qualquer coisa que queira ser um Processador de Dados OBRIGATORIAMENTE tem que ter um método chamado `process`".
- Nós não implementamos o código aqui (tem apenas `pass`), apenas definimos a regra.

#### 2. As Implementações Concretas
Temos três classes que obedecem a este contrato: `NumericProcessor`, `TextProcessor` e `LogProcessor`.

Cada uma delas **herda** de `DataProcessor` e implementa o método `process` à sua maneira:
- **NumericProcessor:** Calcula média e soma.
- **TextProcessor:** Conta palavras e caracteres.
- **LogProcessor:** Verifica se é um erro ou informação.

#### 3. O Polimorfismo em Ação
Onde está a magia? Está no facto de que poderíamos ter uma lista mista destes processadores e mandar todos processarem dados sem saber exatamente qual é qual.

Embora o exemplo do `main` os trate individualmente, a estrutura permite que o sistema cresça. Se amanhã criares um `ImageProcessor`, o resto do sistema não precisa mudar.

### Resultado da Execução (Output)

```text
=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===

Initializing Numeric Processor...
Processing data: [1, 2, 3, 4, 5]
Validation: Numeric data verified
Output: Processed 5 numeric values, sum=15, avg=3.0

Initializing Text Processor...
Processing data: "Hello Nexus World"
Validation: Text data verified
Output: Processed text: 17 characters, 3 words

Initializing Log Processor...
Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ALERT] ERROR level detected: Connection timeout
```

**Explicação:**
- Vê como cada processador recebeu um tipo de dado diferente e produziu um resultado específico, mas todos seguiram a estrutura `validate` -> `process` -> `format_output`.

---

## Parte 3: Exercício 1 - Streams e Coleções Polimórficas (DataStream)

Aqui elevamos o nível. Vamos ver como gerir múltiplos objetos diferentes numa única coleção.

### Análise do Código (`ex1/data_stream.py`)

#### 1. A Classe `DataStream`
Novamente, uma classe base que define métodos comuns como `filter_data` (que todos herdam e usam igual) e métodos abstratos como `process_batch` (que cada um faz à sua maneira).

#### 2. O `StreamProcessor` (O Gerente)
Esta é a parte mais importante:

```python
class StreamProcessor():
    def __init__(self):
        self.streams: Dict[str, DataStream] = {} # Coleção Polimórfica
```

O dicionário `self.streams` guarda objetos. O processador **não sabe** se o objeto lá dentro é um `SensorStream` ou um `TransactionStream`. Ele só sabe que é um `DataStream`.

Quando ele executa:
```python
self.streams[stream_id].process_batch(data_batch)
```
O Python descobre automaticamente, em tempo de execução, qual é o tipo do objeto e chama a versão correta do método `process_batch`. Isso chama-se **Dynamic Dispatch**.

### Resultado da Execução (Output)

```text
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
...
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
...
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...
...
- Sensor data: Sensor analysis: 3 readings processed, avg temp: 22.5°C
```

**Explicação:**
- Repara na secção "Polymorphic Stream Processing". O código pega num stream genérico (`sensor_obj`) e aplica um filtro. O filtro funciona porque está na classe pai. O processamento funciona e é específico do sensor porque foi sobrescrito (overridden) na classe filha.

---

## Parte 4: Exercício 2 - Duck Typing e Pipelines (Nexus Pipeline)

No Python, o polimorfismo vai além da herança. Existe um conceito chamado **Duck Typing**:
> "Se anda como um pato e grasna como um pato, então deve ser um pato."

### Análise do Código (`ex2/nexus_pipeline.py`)

#### 1. Protocolos e Interfaces Implícitas
Aqui temos classes como `InputStage`, `TransformStage` e `OutputStagezz`.
Elas **não herdam** de uma classe pai comum no sentido estrito de código partilhado. Mas todas elas têm um método:
```python
def process(self, data: Any) -> Any:
```
Para o Python, isso é suficiente para serem tratadas de forma igual.

#### 2. O `ProcessingPipeline`
O pipeline tem uma lista de estágios (`self.stages`). Ele percorre a lista e chama `.process()` em cada um.
Não interessa se o estágio é de Input ou Output. Se tem o método `.process()`, o Python executa.

#### 3. O `NexusManager`
Este gestor lida com vários Pipelines (`JSONAdapter`, `CSVAdapter`, etc.). Mais uma vez, ele trata todos como `ProcessingPipeline`. Se um dia quiseres adicionar um `XMLAdapter`, só precisas criar a classe com o método `process`. Não precisas mudar nada no `NexusManager`. **Isto é a base de código flexível e escalável.**

### Resultado da Execução (Output)

```text
=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===
...
Processing JSON data through pipeline...
Input: {"sensor": "temp", "value": 23.5, "unit": "C"}
Output: Processed temperature reading: 23.5°C (Normal range)

Processing CSV data through same pipeline...
Input: "user,action,timestamp"
Output: User activity logged: 1 actions processed
...
```

**Explicação:**
- O mesmo motor de processamento (`NexusManager`) conseguiu lidar com JSON, CSV e Streams em tempo real.
- Ele usou os métodos específicos de cada adaptador para processar os dados, mas o código que chama esses métodos é único e genérico.

---

## Resumo Final

1.  **Herança:** Permite criar uma hierarquia (Pai -> Filho) onde o filho herda comportamentos e pode modificar outros. Garante que todos seguem as mesmas regras.
2.  **Polimorfismo:** Permite usar uma variável genérica (ex: `processador`) para guardar objetos diferentes (`Numerico`, `Texto`) e chamar os mesmos métodos, obtendo comportamentos diferentes.
3.  **Vantagem:** O teu código fica limpo. Em vez de teres 50 `if/else` (se for numero faz isto, se for texto faz aquilo), tens apenas uma chamada de método, e o objeto sabe o que fazer consigo próprio.

Espero que este guia tenha ajudado a desmistificar estes conceitos! O código agora está comentado em inglês para ajudar a relacionar a teoria com a prática.
