resource "linode_instance" "k8s_node" {
  count           = var.instance_count
  label           = "${var.k8s_env}_k8s_node_${count.index + 1}"
  image           = "linode/ubuntu20.04"
  region          = "eu-central"
  type            = "g6-standard-1"
  authorized_keys = [var.my_ssh_key]
}
