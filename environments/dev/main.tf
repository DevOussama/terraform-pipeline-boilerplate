module "example" {
  source      = "git::https://github.com/org/repo.git//modules/example?ref=1.0.0"
  environment = "dev"
}
