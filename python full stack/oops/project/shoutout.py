import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# s="krishnaveni for being a class topper"
# speaker.Speak(f"congratulations to {s}")
s=["jayasri","yamini","devika","krishnaveni","poojitha"]
for i in s:
    speaker.Speak(f"Toppers andi babu {i}")