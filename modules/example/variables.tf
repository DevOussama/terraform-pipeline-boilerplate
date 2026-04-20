variable "environment" {
  description = "The deployment environment (dev, staging, prod)"
  type        = string
}

variable "module_name" {
  description = "Name of the module"
  type        = string
  default     = "example"
}
