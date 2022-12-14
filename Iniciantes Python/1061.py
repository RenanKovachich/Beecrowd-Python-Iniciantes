dia_ini = input()
time_ini = input()
dia_final = input()
time_final = input()

dia_int = [str(x) for x in dia_ini.split(' ')]
day_i = int(dia_int[1])

time_int = [str(y) for y in time_ini.split(' ')]
hours_i = int(time_int[0])
minutes_i = int(time_int[2])
seconds_i = int(time_int[4])

dia_int2 = [str(w) for w in dia_final.split(' ')]
day_final = int(dia_int2[1])

time_int2 = [str(z) for z in time_final.split(' ')]
hours_f = int(time_int2[0])
minutes_f = int(time_int2[2])
seconds_f = int(time_int2[4])

time_inicial = (hours_i*3600) + (minutes_i*60) + seconds_i
time_end = (hours_f*3600) + (minutes_f*60) + seconds_f
time_total = time_end - time_inicial

hrs = time_total // 3600
mns = (time_total - hrs*3600) // 60
seconds = (time_total - hrs*3600 - mns*60)
dias = day_final - day_i
if hrs < 0:
    dias -= 1
    hrs += 24

print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(hrs))
print('{} minuto(s)'.format(mns))
print('{} segundo(s)'.format(seconds))
