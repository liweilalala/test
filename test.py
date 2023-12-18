import subprocess

# 执行命令行
command = """kubectl get service -n kourier-system -o=jsonpath='{.items[0].spec.clusterIP}'"""
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)

# 获取输出
output = result.stdout
print("Command Output:\n", output)
