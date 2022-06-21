ticks = 0

def start(devs, auto = True):
   global ticks
   while True:
      if not auto:
         input()
      success = True
      for dev in devs:
         success = success and dev.step()
      if success:
         ticks += 1
          
      else:
         break
      
   print("ExecuÃ§Ã£o finalizada em", ticks, "passos.")