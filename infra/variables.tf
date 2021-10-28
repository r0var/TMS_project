variable "instance_count" {
  default = "4"
}

variable "linode_token" {
  description = "token for Linode API"
}

variable "my_ssh_key" {
  description = "ssh public key for instances"
}

variable "k8s_env" {
  description = "Environment name"
}
