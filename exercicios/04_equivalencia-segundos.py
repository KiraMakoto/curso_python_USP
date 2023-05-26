segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = segundos // 86400
horas = (segundos % 86400)//3600
minutos = ((segundos % 86400)%3600)//60
segundos = ((segundos % 86400)%3600)%60
print(dia,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
