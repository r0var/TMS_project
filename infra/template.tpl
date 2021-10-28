[all]
%{ for ip in public_ip ~}
node${index(public_ip, ip) + 1} ansible_host=${ip} ip=${ip}
%{ endfor ~}

[kube_control_plane]
node1
%{ if length(public_ip) > 1 }
[etcd]
node2%{ else }
[etcd]
node1
%{ endif }

[kube_node]%{ if length(public_ip) > 2}%{ for ip in public_ip ~}%{ if index(public_ip, ip) > 1}
node${index(public_ip, ip) + 1}%{ endif }%{ endfor ~}%{ else }
node1
%{ endif }

[calico_rr]

[k8s_cluster:children]
kube_control_plane
kube_node
calico_rr
