resource "local_file" "AnsibleInventory" {
  content = templatefile("template.tpl",
  {
    public_ip = flatten(linode_instance.k8s_node.*.ipv4)
  }
  )
  filename = "inventory.ini"
}
