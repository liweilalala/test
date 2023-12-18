import subprocess

# 执行命令行
command = """kubectl get service -n kourier-system -o=jsonpath='{.items[0].spec.clusterIP}'"""
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)

# 获取输出
output = result.stdout
print("Command Output1:\n", output)
command = """kubectl get route test-hello -n test1 -o=jsonpath='{.status.url}'"""
result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)

# 获取输出
output = result.stdout
print("Command Output2:\n", output)
