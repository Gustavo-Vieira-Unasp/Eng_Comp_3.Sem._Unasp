import time
import random
from collections import deque

class FilaDeAtendimento:
    def __init__(self):
        self.fila = deque()
        self.tempo_de_espera() = 0
        self.pacientes_atendidos() = 0

    def chegada_paciente(self, id_paciente, tempo_de_chegada):
        self.fila.append(
            {
                'id' : id_paciente,
                'chegada' : tempo_de_chegada,
                'tempo consuta' : random.ranint(1, 5)
            }
        )
        print(f"Paciente {id_paciente} entrou na fila {tempo_de_chegada}")

    def antender_proximo(self, tempo_atual):
        if not self.fila:
            return None
        
        paciente = self.fila.popleft()
        tempo_espera = tempo_atual - paciente['chegada']
        self.tempo_total_espera += tempo_espera
        self.pacientes_atendidos += 1

        print(f"Paciente {paciente['id']} atendido em {tempo_atual}")
        print(f"Tempo de espera: {tempo_espera}")

    def tempo_medio_espera(self):
        if self.pacientes_atendidos == 0:
            return 0
        
        return self.tempo_total_espera/self.pacientes_atendidos
    
fila_de_atendimento = FilaDeAtendimento()
tempo_simulacao = 20
tempo_atual = 0
ultimo_paciente = 0

while tempo_atual < tempo_simulacao:
    if random.random() < 0.3 :
        fila_de_atendimento.chegada_paciente(ultimo_paciente+1, tempo_atual)
        ultimo_paciente += 1

    if random.random() < 0.5 :
        tempo_consulta = fila_de_atendimento.antender_proximo(tempo_atual)

    tempo_atual += 1
    time.sleep(0.5)

print(f"\nTempo médio de espera: {fila_de_atendimento.tempo_medio_espera()}")
print(f"\nPacientes atendidos: {fila_de_atendimento.pacientes_atendidos}")
print(f"\nPacientes para serem atendidos: {len(fila_de_atendimento)}")