import subprocess

global ress

def DetailsEcho(name, roll):
    command = "echo "+name+":"+roll
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            ress = result
            print("Echo command run successfully")
            print(result.stdout)
        else:
            print("Echo command failed: ")
            print(result.stderr)

    except Exception as e:
        print("Error:", e)


def GetIP():
    print()


DetailsEcho("Ravi", "18")