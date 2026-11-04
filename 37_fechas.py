import datetime as dt
print(f"fecha de hoy: {dt.date.today()}")
print(f"hora acutal: {dt.datetime.now()}")
f_posterior=dt.datetime.now()+dt.timedelta(days=20,hours=60)

print(f_posterior)

fechahora_actual=dt.datetime.now()
print(f"La fecha y hora actuales {dt.datetime.strftime(fechahora_actual,"%d/%m/%Y - %H:%M")}")

