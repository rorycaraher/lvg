provider "google" {
  project = var.project
  region  = var.region
}

variable "project" {
  description = "The GCP project to use"
  type        = string
}

variable "region" {
  description = "The GCP region to use"
  type        = string
  default     = "us-central1"
}
