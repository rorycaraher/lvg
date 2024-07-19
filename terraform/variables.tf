variable "project" {
  description = "The GCP project to use"
  type        = string
}

variable "static_site_bucket_name" {
  description = "The name of the static site bucket"
  type        = string
  default     = "static-site"
}

variable "db_password" {
  description = "The password for the database user"
  type        = string
}

variable "pubsub_topic_name" {
  description = "The name of the Pub/Sub topic"
  type        = string
  default     = "level_values"
}

variable "region" {
  description = "The GCP region to use"
  type        = string
  default     = "europe-west1"
}
