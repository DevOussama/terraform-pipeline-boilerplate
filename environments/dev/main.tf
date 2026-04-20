module "example" {
  source      = "git::https://github.com/org/repo.git//modules/example?ref=v1.0.0"
  environment = "dev"
}
