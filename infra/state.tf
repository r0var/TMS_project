terraform {
  backend "s3" {
    bucket                      = "r0varstorage"
    key                         = "dev.tfstate"
    region                      = "eu-central-1"
    endpoint                    = "eu-central-1.linodeobjects.com"
    skip_credentials_validation = true
  }
}
