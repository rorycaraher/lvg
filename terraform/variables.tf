variable "project" {
  description = "The GCP project to use"
  type        = string
}

variable "region" {
  description = "The GCP region to use"
  type        = string
  default     = "europe-west1"
}
