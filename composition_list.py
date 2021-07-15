#! coding: utf-8

cluster = {"region": ["shanghai"], "namespace": ["default", "kube-system", "gitlab"], "pod_num": [30, 40, 10]}
print(cluster)

composition_list = map(list, zip(cluster["region"] * 3, cluster["namespace"], cluster["pod_num"]))
print(composition_list)

"""
{'region': ['shanghai'], 'namespace': ['default', 'kube-system', 'gitlab'], 'pod_num': [30, 40, 10]}

实现转换为如下的格式

shanghai default 30
shanghai kube-system 40
shanghai gitlab 10
"""
for item in composition_list:
    print(item[0], item[1], item[2])
