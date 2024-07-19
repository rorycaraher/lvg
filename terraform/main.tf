
provider "google" {
  project = var.project
  region  = var.region
}

output "debug_project" {
  value = var.project
}

output "debug_region" {
  value = var.region
}
